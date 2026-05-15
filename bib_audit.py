import re, sys

BIB = r'C:/Users/ZYJ/microneedle-review/references.bib'
TEX = r'C:/Users/ZYJ/microneedle-review/main.tex'

with open(BIB, 'r', encoding='utf-8') as f:
    bib = f.read()
with open(TEX, 'r', encoding='utf-8') as f:
    tex = f.read()

errors = []
passed = []

# ── 1. Non-ASCII chars ──────────────────────────────────────────
non_ascii = [i for i, c in enumerate(bib) if ord(c) > 127]
if non_ascii:
    errors.append(f'[FAIL] 1. Non-ASCII: {len(non_ascii)} chars remain')
else:
    passed.append('[PASS] 1. Non-ASCII: zero')

# ── 2. Entry opener inline % comments ──────────────────────────
openers_bad = re.findall(r'^@\w+\{[^,\n]+,[ \t]*%[^\n]+', bib, re.MULTILINE)
if openers_bad:
    errors.append(f'[FAIL] 2. Opener % comments: {openers_bad[:2]}')
else:
    passed.append('[PASS] 2. Entry opener lines: clean')

# ── 3. Required fields (BibTeX-style) ──────────────────────────
entry_re = re.compile(r'@(\w+)\{([\w-]+),(.*?)\n\}', re.DOTALL)
entries = entry_re.findall(bib)
field_re = re.compile(r'^[ \t]*(\w+)\s*=', re.MULTILINE)
required = {
    'article':       ['author', 'title', 'journal', 'year'],
    'inproceedings': ['author', 'title', 'booktitle', 'year'],
    'book':          ['author', 'title', 'publisher', 'year'],
}
missing_fields = []
for etype, ekey, body in entries:
    fields = {m.lower() for m in field_re.findall(body)}
    for f in required.get(etype.lower(), []):
        if f not in fields:
            missing_fields.append(f'{ekey}: [{f}]')
if missing_fields:
    errors.append(f'[FAIL] 3. Missing fields: {missing_fields[:5]}')
else:
    passed.append(f'[PASS] 3. Required fields: all {len(entries)} entries complete')

# ── 4. Brace balance ────────────────────────────────────────────
depth = 0
fail_pos = -1
for i, c in enumerate(bib):
    if c == '{':
        depth += 1
    elif c == '}':
        depth -= 1
        if depth < 0:
            fail_pos = i
            break
if fail_pos >= 0 or depth != 0:
    errors.append(f'[FAIL] 4. Brace balance: depth={depth} fail_pos={fail_pos}')
else:
    passed.append('[PASS] 4. Brace balance: fully balanced')

# ── 5. main.tex commands ────────────────────────────────────────
needles = [
    ('\\bibliography{references}', 'bibliography{references}'),
    ('\\bibliographystyle{elsarticle-num}', 'bibliographystyle{elsarticle-num}'),
    ('\\clearpage', 'clearpage'),
]
for needle, label in needles:
    if needle in tex:
        passed.append(f'[PASS] 5. tex has {label}')
    else:
        errors.append(f'[FAIL] 5. tex MISSING {label}')

# Verify clearpage appears BEFORE bibliography
cp_idx = tex.rfind('\\clearpage')
bib_idx = tex.find('\\bibliography{references}')
if cp_idx >= 0 and bib_idx >= 0:
    if cp_idx < bib_idx:
        passed.append('[PASS] 5. clearpage is before bibliography')
    else:
        errors.append('[FAIL] 5. clearpage appears AFTER bibliography')

# ── 6. Cite-key cross-reference ─────────────────────────────────
bib_keys = {e[1] for e in entries}
all_cite_keys = set()
pos = 0
while True:
    idx = tex.find('\\cite{', pos)
    if idx < 0:
        break
    end = tex.find('}', idx + 6)
    block = tex[idx + 6:end]
    for k in block.split(','):
        all_cite_keys.add(k.strip())
    pos = idx + 1

missing_keys = all_cite_keys - bib_keys
if missing_keys:
    errors.append(f'[FAIL] 6. {len(missing_keys)} cite keys missing in bib: {sorted(missing_keys)[:5]}')
else:
    passed.append(f'[PASS] 6. Cite-key cross-ref: all {len(all_cite_keys)} keys found in bib')

# ── 7. Zip contents ─────────────────────────────────────────────
import zipfile, os
ZIP = r'C:/Users/ZYJ/microneedle-review/overleaf_upload.zip'
required_files = ['main.tex', 'references.bib', 'elsarticle.cls', 'elsarticle-num.bst',
                  'fig_01_system_chain.png', 'fig_02_fabrication.png',
                  'fig_03_modality_radar.png', 'fig_04_biomarkers.png',
                  'fig_05_circuits.png', 'fig_06_intelligence.png', 'graphical_abstract.png']
if os.path.exists(ZIP):
    with zipfile.ZipFile(ZIP) as zf:
        zipped = {os.path.basename(n) for n in zf.namelist()}
    missing_zip = [f for f in required_files if f not in zipped]
    if missing_zip:
        errors.append(f'[FAIL] 7. Zip missing: {missing_zip}')
    else:
        passed.append(f'[PASS] 7. Zip: all {len(required_files)} files present')
else:
    errors.append('[FAIL] 7. overleaf_upload.zip NOT FOUND')

# ── Summary ─────────────────────────────────────────────────────
print('\n'.join(passed))
if errors:
    print()
    print('\n'.join(errors))
    print(f'\nRESULT: FAIL ({len(errors)} errors)')
    sys.exit(1)
else:
    print(f'\nRESULT: ALL {len(passed)} CHECKS PASSED')
