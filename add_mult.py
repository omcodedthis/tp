import glob, re

def add_multiplicity(p):
    with open(p, 'r', encoding='utf-8') as f: lines = f.readlines()
    changed = False
    for i in range(len(lines)):
        s = lines[i]
        match = re.search(r'^(\s*)(\w+)\s+((?:\*|-|\.)(?:-|\.)+>)\s+("\d+"|"\*")\s+(\w+)\s*:\s*(.*)$', s)
        if match:
            indent, w1, arr, right_mult, w2, comment = match.groups()
            new_s = f'{indent}{w1} "1" {arr} {right_mult} {w2} : {comment}\n'
            lines[i] = new_s
            changed = True
    if changed:
        print(f"Added mult to {p}")
        with open(p, 'w', encoding='utf-8') as f: f.writelines(lines)

for p in glob.glob('docs/diagrams/**/*Architecture.puml', recursive=True): add_multiplicity(p)
for p in glob.glob('docs/diagrams/**/*.puml', recursive=True):
    if "architecture" in p.lower():
        add_multiplicity(p)
