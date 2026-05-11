import os, yaml, re, sys
from pathlib import Path
from collections import Counter

BASE = Path("D:/llm-wiki-wanghai/wiki")

def read_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                return fm, parts[1], parts[2]
            except:
                return {}, parts[1] if len(parts) >= 2 else "", parts[2] if len(parts) >= 3 else ""
    return {}, "", content

def classify_confidence(fm):
    """Conservative: default low unless multiple quality sources."""
    sources = fm.get('sources', [])
    if not sources:
        return 'low'
    if not isinstance(sources, list):
        sources = [sources]

    num = len(sources)
    has_book = False
    has_academic = False

    for s in sources:
        sl = str(s).lower()
        # Book indicators
        if any(kw in sl for kw in ['book', 'press', 'publishing', 'edition', 'isbn',
                                     'wiley', 'cambridge', 'oxford', 'princeton',
                                     'mit press', 'sage', 'routledge', 'springer',
                                     'elsevier', 'mcgraw', 'pearson', '大学出版',
                                     '出版社', '教材', '第', '卷', '版']):
            has_book = True
        # Academic indicators
        if any(kw in sl for kw in ['journal', 'review', 'doi', 'vol', 'et al',
                                     'nber', 'econometrica', 'quarterly',
                                     'academy of management', 'forests',
                                     'development and change', 'ocean',
                                     '生态学报', '自然资源学报', '管理世界', '经济研究',
                                     '中国社会科学', '资源与产业', '中国人口',
                                     '.pdf']):
            has_academic = True

    if num >= 3 and (has_academic or has_book):
        return 'high'
    elif num >= 2 and has_academic:
        return 'high'
    elif num >= 1 and has_book:
        return 'medium'
    elif num >= 1 and has_academic:
        return 'medium'
    elif num >= 2:
        return 'medium'
    else:
        return 'low'

def classify_decay(fm, filepath, body):
    """Conservative decay: use the page's KNOWLEDGE TYPE as primary signal."""
    tags = fm.get('tags', [])
    if not isinstance(tags, list):
        tags = []
    tags_text = ' '.join(str(t) for t in tags)
    path_str = str(filepath)
    status = fm.get('status', '')
    body_head = '\n'.join(body.split('\n')[:50]) if body else ''
    # Body text for content-type matching only (not case/location names)
    body_for_content = body_head
    # File identity (tags + filename) for case/location matching
    identity_text = tags_text + ' ' + str(filepath.stem)

    # === CORE SLOW: definitional / axiomatic / timeless theory ===
    slow_definitive = [
        '定义', '公理', 'axiom', 'welfare theorem', '福利定理',
        'gdp核算恒等式', 'gdp三种核算', '国民收入核算衍生',
        '货币数量论', '古典二分法', '货币中性', '费雪效应',
        'solow增长模型', '平衡增长路径', '增长核算',
        'islm模型', 'ad-as模型', 'mundell-fleming', 'phillips曲线',
        'capm', '证券市场线', '资本市场线', 'black-scholes', 'mm定理',
        '期望效用理论', '无套利定价理论基础', '一般均衡',
        '预算约束', '无差异曲线', '边际替代率', 'slutsky方程',
        '生产函数', '成本函数', '利润最大化',
        '纳什均衡', '博弈论',
        'coase定理', 'pigou税', '外部性理论',
        'maslow需求层次', 'herzberg双因素', '期望理论',
        'porter五力', 'swot分析', '管理职能', '科学管理', '科层制',
        '利益相关者理论',
        '商业模式分析框架-琦谈', '利润对增量收入的敏感度',
    ]

    # === STRONG SLOW: theoretical frameworks, stable knowledge ===
    slow_framework = [
        '理论', '原理', '方法论', 'methodology', '思想史',
        '框架', 'framework', '分析框架',
        '分类体系', '分类', '类型学', 'typology',
        '核算方法', '核算体系', 'accounting methodology',
        '生态产品价值实现机制',  # the 3-path framework, not a specific case
        '机制复合体框架',
        '生态补偿十对关系',
        '生态产品分类体系',
        '两山理论',
        '生态补偿的pigou与coase路径',
        'sa-sna-ega分析框架',
        'mendelow权力-利益矩阵',
        '村集体三重身份',
    ]

    # === CORE FAST: specific cases, current events, rapidly evolving ===
    fast_definitive = [
        '案例', 'case study',
        '淄博', '丽水', '韶关', '南平', '新安江', '萍乡', '三江源',
        '始兴', '南雄', '翁源',
        'covid', '新冠', '流行病', 'pandemic',
        'vep2.0', '碳汇交易', '碳边境', '气候俱乐部',
        '试点',
        '资产管理vs投资银行', '淄博烧烤',
        '中美', 'us-china', '产业竞争',
        '工业基础型', '工业基础型生态地区',
        '工业城市',
    ]

    # === FAST: evolving policy/market/tech topics ===
    fast_applied = [
        '政策工具', '政策建议', '制度建议',
        '绿色金融', '绿色债券', 'esg基金', '社会责任投资',
        '数字', 'digital', 'ai ', '人工智能',
        '创新', 'innovation', '技术', 'technology',
        '平台', 'platform', '交易', 'trading',
        '碳汇', '碳交易', '碳市场', '碳税',
        '激励兼容', '利益冲突', '博弈推演',
    ]

    slow_score = 0
    fast_score = 0

    # slow_definitive + slow_framework: match against all text (identity + body)
    all_text = identity_text + ' ' + body_for_content

    for kw in slow_definitive:
        if kw in all_text.lower():
            slow_score += 4
    for kw in slow_framework:
        if kw in all_text.lower():
            slow_score += 3

    # fast_definitive (case names, locations): match ONLY against identity (tags + filename)
    # This prevents a theory page from becoming "fast" just because it mentions 丽水 as an example
    for kw in fast_definitive:
        if kw in identity_text.lower():
            fast_score += 4

    # fast_applied (content type): match against all text
    for kw in fast_applied:
        if kw in all_text.lower():
            fast_score += 2

    # Status signals
    if status == 'foundation':
        slow_score += 2
    elif status == 'seedling':
        fast_score += 2
    elif status == 'stub':
        fast_score += 1

    # Very recent creation leans fast
    created = fm.get('created', '')
    if str(created).startswith('2026'):
        fast_score += 2
    elif str(created).startswith('2025'):
        fast_score += 1

    # Older stable content leans slow
    if str(created).startswith('2024') or str(created).startswith('2023'):
        slow_score += 1

    diff = slow_score - fast_score
    if diff >= 4:
        return 'slow'
    elif diff <= -4:
        return 'fast'
    else:
        return 'medium'

def apply_to_file(filepath):
    fm, fm_raw, body = read_frontmatter(filepath)
    if 'confidence' in fm and 'decay_category' in fm:
        return False

    updates = {}
    if 'confidence' not in fm:
        updates['confidence'] = classify_confidence(fm)
    if 'decay_category' not in fm:
        updates['decay_category'] = classify_decay(fm, filepath, body)

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    old_fm = parts[1]

    for field_name, field_value in updates.items():
        if f"\n{field_name}:" not in old_fm and not old_fm.startswith(f"{field_name}:"):
            fm_lines = old_fm.split('\n')
            insert_idx = len(fm_lines)
            for i, line in enumerate(fm_lines):
                stripped = line.strip()
                # Skip leading empty lines (artifact of --- delimiter)
                if stripped == '' and i == 0:
                    continue
                if stripped.startswith('status:') or stripped.startswith('---'):
                    insert_idx = i
                    break
                # Insert before first empty line after content starts
                if stripped == '' and i > 0:
                    insert_idx = i
                    break
            fm_lines.insert(insert_idx, f'{field_name}: {field_value}')
            old_fm = '\n'.join(fm_lines)

    new_content = '---' + old_fm + '---' + parts[2]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fill_confidence.py <dir> [--dry-run]")
        sys.exit(1)

    target = BASE / sys.argv[1]
    dry_run = '--dry-run' in sys.argv

    if not target.exists():
        print(f"Directory not found: {target}")
        sys.exit(1)

    files = sorted(target.glob("*.md"))
    results = []

    for f in files:
        fm, _, body = read_frontmatter(f)
        conf = classify_confidence(fm)
        decay = classify_decay(fm, f, body)
        sources = fm.get('sources', [])
        if not isinstance(sources, list):
            sources = [sources]
        if 'confidence' not in fm or 'decay_category' not in fm:
            results.append((f.stem, conf, decay, len(sources)))

    out_path = BASE.parent / 'scripts' / f'_dryrun_{target.name}.txt'
    with open(out_path, 'w', encoding='utf-8') as out:
        for name, conf, decay, ns in results:
            out.write(f'{name}\tconf={conf}\tdecay={decay}\tsrc={ns}\n')
        out.write(f'\nConfidence: {dict(Counter(r[1] for r in results))}\n')
        out.write(f'Decay: {dict(Counter(r[2] for r in results))}\n')
        out.write(f'Total: {len(results)}\n')

    print(f"Written {len(results)} entries to scripts/_dryrun_{target.name}.txt")
    print(f"Confidence: {dict(Counter(r[1] for r in results))}")
    print(f"Decay: {dict(Counter(r[2] for r in results))}")

    if dry_run:
        print("DRY RUN — no changes applied.")
    else:
        updated = 0
        for f in files:
            if apply_to_file(f):
                updated += 1
        print(f"Applied changes to {updated} files.")
