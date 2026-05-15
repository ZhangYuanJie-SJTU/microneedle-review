import re

with open(r'C:/Users/ZYJ/microneedle-review/main.tex', 'r', encoding='utf-8') as f:
    tex = f.read()
with open(r'C:/Users/ZYJ/microneedle-review/references.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

# clearpage vs bibliography ordering
cp_positions = [m.start() for m in re.finditer(r'\\clearpage', tex)]
bib_cmd_pos = tex.find(r'\bibliography{references}')
print('clearpage positions:', cp_positions)
print('bibliography{references} at:', bib_cmd_pos)
for pos in cp_positions:
    print('  clearpage before bib?', pos < bib_cmd_pos, '| diff =', bib_cmd_pos - pos)

# Fogh-Andersen2022
print()
present = 'Fogh-Andersen2022' in bib
print('Fogh-Andersen2022 in bib (string search):', present)
if present:
    idx = bib.find('Fogh-Andersen2022')
    print(repr(bib[idx-2:idx+80]))

# All keys with hyphen
keys_hyphen = re.findall(r'@\w+\{([\w-]+),', bib)
print('Total keys parsed (incl hyphen):', len(keys_hyphen))
fogh = [k for k in keys_hyphen if 'ogh' in k.lower()]
print('Fogh-like keys:', fogh)

# Cite keys in tex that use hyphen
tex_cites = []
pos = 0
while True:
    idx = tex.find(r'\cite{', pos)
    if idx < 0:
        break
    end = tex.find('}', idx + 6)
    for k in tex[idx+6:end].split(','):
        tex_cites.append(k.strip())
    pos = idx + 1

hyphen_cites = [k for k in tex_cites if '-' in k]
print()
print('Cite keys with hyphen:', hyphen_cites)

# Cross-ref with hyphen-aware
bib_keys_all = set(keys_hyphen)
missing = set(tex_cites) - bib_keys_all
print()
print('Missing from bib (hyphen-aware):', sorted(missing))
