#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""同日刷新 2026-09-24 榜单快照：不新增日期条目，只更新数字/排序/topic（保持 11 席位与 badge 不变）"""
import json, re

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'
with open(path, encoding='utf-8') as f:
    data = json.load(f)

day = data['days'][0]
assert day['date'] == '2026-09-24' and day['label'] == '今天', f"days[0] 不是今天: {day['date']} {day['label']}"

# 09-24 20:37 重新抓取的快照（starsToday 为 GitHub 当日累计值）
fresh = {
    'hindsight':                    {'stars': '26,963',  'forks': '2,533',  'starsToday': '1,607'},
    'superpowers':                  {'stars': '290,994', 'forks': '26,037', 'starsToday': '606'},
    'harness-sdk':                  {'stars': '8,081',   'forks': '1,218',  'starsToday': '463'},
    'ai-engineering-from-scratch':  {'stars': '55,943',  'forks': '9,873',  'starsToday': '310'},
    'FxEmbed':                      {'stars': '5,270',   'forks': '243',    'starsToday': '165'},
    'lap':                          {'stars': '2,696',   'forks': '165',    'starsToday': '71'},
    'ax':                           {'stars': '9,714',   'forks': '476',    'starsToday': '1,376'},
    'univer':                       {'stars': '17,123',  'forks': '1,495',  'starsToday': '1,060'},
    'financial-services':           {'stars': '37,208',  'forks': '5,406',  'starsToday': '510'},
    'mvt':                          {'stars': '14,607',  'forks': '1,390',  'starsToday': '275'},
    'treg':                         {'stars': '2,955',   'forks': '251',    'starsToday': '470'},
}

by_name = {p['name']: p for p in day['projects']}
assert set(by_name) == set(fresh), f"席位不符: 榜上 {sorted(by_name)} / 快照 {sorted(fresh)}"

changed = []
for name, snap in fresh.items():
    p = by_name[name]
    old = (p['stars'], p['starsToday'])
    # 亮点行里括注的历史星级（如「7,525★ → 9,653★」）也要跟着改
    p['description'] = re.sub(r'→ [\d,]+★', f"→ {snap['stars']}★", p['description'])
    p['description'] = re.sub(r'今日 \+[\d,]+★', f"今日 +{snap['starsToday']}★", p['description'])
    p.update(snap)
    if old != (snap['stars'], snap['starsToday']):
        changed.append(f"{name}: {old[0]}★/+{old[1]} → {snap['stars']}★/+{snap['starsToday']}")

# 按日增重排（新面孔在前、连登在后），编号重排
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

nf = sorted([p for p in day['projects'] if p['badge'] == '新面孔'], key=lambda p: -_today(p))
st = sorted([p for p in day['projects'] if p['badge'] == '连登'], key=lambda p: -_today(p))
day['projects'] = nf + st
for i, p in enumerate(day['projects'], 1):
    p['rank'] = i

# topic 行的数字同步（逐项替换，缺一个就报错，避免静默漂移）
topic_subs = [
    ('（+474★）', '（+606★）'), ('（+310★）', '（+310★）'),
    ('（+115★）', '（+463★）'), ('（+165★）', '（+165★）'),
    ('（+71★）', '（+71★）'), ('（+1,543★）', '（+1,376★）'),
    ('（+1,142★）', '（+1,060★）'), ('（+664★）', '（+510★）'),
    ('（+543★）', '（+275★）'), ('（+506★）', '（+470★）'),
]
topic = data['topic']
for old, new in topic_subs:
    assert old in topic, f"topic 里找不到 {old}"
    topic = topic.replace(old, new, 1)
topic = re.sub(r'9,653★', '9,714★', topic)
topic = re.sub(r'16,941★', '17,123★', topic)
topic = re.sub(r'37,187★', '37,208★', topic)
topic = topic.replace('（榜单于 09-24 20:37 二次刷新）', '')
data['topic'] = topic.rstrip() + '（榜单于 09-24 20:37 二次刷新，同日重取快照）'

assert len(data['days']) == 80, f"日期条目数被改了: {len(data['days'])}"
assert day['date'] == '2026-09-24' and day['label'] == '今天'
assert data['lastUpdated'] == '2026-09-24'
nf_n = sum(1 for p in day['projects'] if p['badge'] == '新面孔')
st_n = sum(1 for p in day['projects'] if p['badge'] == '连登')
assert nf_n == 6 and st_n == 5, f"栏位异常 {nf_n}/{st_n}"

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"同日刷新完成 | 席位 {len(day['projects'])}（新面孔 {nf_n} / 连登 {st_n}）| 日期条目仍为 {len(data['days'])}")
print("数字有变化的:")
for c in changed:
    print("  -", c)
print("\n刷新后榜单:")
for p in day['projects']:
    print(f"  [{p['badge']}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★")
