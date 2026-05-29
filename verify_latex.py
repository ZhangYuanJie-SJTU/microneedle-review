import re

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Check 1: begin/end balance
begins = len(re.findall(r'\\begin\{', content))
ends = len(re.findall(r'\\end\{', content))
status = 'PASS' if begins == ends else 'FAIL'
print(f'[CHECK 1] begin/end balance: {begins} begins, {ends} ends - {status}')

# Check 2: Structure
sections = re.findall(r'\\section\{([^}]+)\}', content)
subsections = re.findall(r'\\subsection\{([^}]+)\}', content)
print(f'[CHECK 2] Structure: {len(sections)} sections, {len(subsections)} subsections')
for i, s in enumerate(sections):
    print(f'  Section {i+1}: {s}')

# Check 3: Figure cross-refs
fig_labels = set(re.findall(r'\\label\{(fig:[^}]+)\}', content))
fig_refs = set(re.findall(r'\\ref\{(fig:[^}]+)\}', content))
orphan_figs = fig_labels - fig_refs
missing_figs = fig_refs - fig_labels
print(f'[CHECK 3] Figure labels: {len(fig_labels)}, refs: {len(fig_refs)}')
if orphan_figs:
    print(f'  ORPHAN labels: {orphan_figs}')
if missing_figs:
    print(f'  MISSING labels: {missing_figs}')
if not orphan_figs and not missing_figs:
    print('  All figure cross-references OK')

# Check 4: Table cross-refs
tab_labels = set(re.findall(r'\\label\{(tab:[^}]+)\}', content))
tab_refs = set(re.findall(r'\\ref\{(tab:[^}]+)\}', content))
orphan_tabs = tab_labels - tab_refs
missing_tabs = tab_refs - tab_labels
print(f'[CHECK 4] Table labels: {len(tab_labels)}, refs: {len(tab_refs)}')
if orphan_tabs:
    print(f'  ORPHAN labels: {orphan_tabs}')
if missing_tabs:
    print(f'  MISSING labels: {missing_tabs}')

# Check 5: Abstract word count
abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
if abstract_match:
    text = re.sub(r'\\[a-zA-Z]+\{[^}]*\}|\\[a-zA-Z]+|\{|\}|~', ' ', abstract_match.group(1))
    words = [w for w in text.split() if w.strip()]
    status = 'PASS' if len(words) <= 300 else f'EXCEEDS ({len(words)})'
    print(f'[CHECK 5] Abstract words: {len(words)} / 300 - {status}')

# Check 6: Highlights
hl_start = content.find('\\begin{highlights}')
hl_end = content.find('\\end{highlights}')
if hl_start >= 0 and hl_end >= 0:
    hl_text = content[hl_start:hl_end]
    items = re.findall(r'\\item ', hl_text)
    status = 'PASS' if 3 <= len(items) <= 5 else f'CHECK ({len(items)} items)'
    print(f'[CHECK 6] Highlights: {len(items)} items - {status}')

# Check 7: Citation keys
cites = re.findall(r'\\cite\{([^}]+)\}', content)
cite_keys = set()
for c in cites:
    for k in c.split(','):
        cite_keys.add(k.strip())
print(f'[CHECK 7] Unique cite keys: {len(cite_keys)}')

# Check 8: linenumbers
if '\\linenumbers' in content:
    print('[CHECK 8] linenumbers: PRESENT - PASS')
else:
    print('[CHECK 8] linenumbers: MISSING - FAIL')

# Check 9: bibliography style
if 'elsarticle-num' in content:
    print('[CHECK 9] bibliographystyle: elsarticle-num - PASS')
else:
    print('[CHECK 9] bibliographystyle: NOT FOUND - FAIL')

# Check 10: New v4.2.0 sections
new_sections = [
    'Technology History',
    'Measurement Instrument Chain',
    'Design Decision Guide',
    'Electrochemical Measurement Fundamentals',
    'Modality Selection Guide',
    'End-to-End System Teardowns',
    'Commercialization Landscape',
    'Open Questions'
]
print('[CHECK 10] New v4.2.0 sections:')
for s in new_sections:
    status = 'PRESENT' if s in content else 'MISSING'
    print(f'  {s}: {status}')

# Check 11: New tables
new_tables = ['tab:design_guide', 'tab:modality_comparison', 'tab:commercial', 'tab:open_questions']
print('[CHECK 11] New v4.2.0 tables:')
for t in new_tables:
    status = 'PRESENT' if t in content else 'MISSING'
    print(f'  {t}: {status}')

# Check 12: New figures
new_figs = ['fig:timeline']
print('[CHECK 12] New v4.2.0 figure references:')
for f in new_figs:
    status = 'PRESENT' if f in content else 'MISSING'
    print(f'  {f}: {status}')

print()
print('=== VERIFICATION COMPLETE ===')
