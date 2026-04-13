import os, glob

def fix(p):
    with open(p, 'r', encoding='utf-8') as f: lines = f.readlines()
    changed = False
    for i in range(len(lines)):
        if '++ ++ : getArg()' in lines[i]:
            lines[i] = lines[i].replace('++ ++ : getArg()', '++ : getArg()')
            changed = True
    if changed:
        with open(p, 'w', encoding='utf-8') as f: f.writelines(lines)

for path in glob.glob('docs/diagrams/**/*.puml', recursive=True): fix(path)
