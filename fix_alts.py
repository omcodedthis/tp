import os, glob

def fix(p):
    with open(p, 'r', encoding='utf-8') as f: lines = f.readlines()
    for i in range(len(lines)):
        s = lines[i].strip()
        if s.startswith('alt '):
            # check what's inside
            has_else = False
            depth = 1
            for j in range(i+1, len(lines)):
                 ts = lines[j].strip()
                 if ts.startswith('alt ') or ts.startswith('opt ') or ts.startswith('loop '): depth += 1
                 elif ts == 'end':
                     depth -= 1
                     if depth == 0: break
                 elif ts.startswith('else ') or ts == 'else':
                     if depth == 1: has_else = True
            if not has_else:
                 lines[i] = lines[i].replace('alt ', 'opt ')
    with open(p, 'w', encoding='utf-8') as f: f.writelines(lines)

for path in glob.glob('docs/diagrams/**/*.puml', recursive=True): fix(path)
print('Done!')
