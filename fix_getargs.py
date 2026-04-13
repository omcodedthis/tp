import os, glob, re

def fix(p):
    with open(p, 'r', encoding='utf-8') as f: lines = f.readlines()
    changed = False
    for i in range(len(lines)):
        s = lines[i]
        if 'getArg(' in s and ',' in s and '++ :' in s:
            # e.g.: handler -> cmd ++ : getArg("n"), getArg("i")
            # Convert to: handler -> cmd ++ : getArg() \n note right : there can be multiple parameters retrieved
            num_args = len(re.findall(r'getArg\(', s))
            if num_args > 1:
                new_str = re.sub(r':.*', '++ : getArg()', s)
                if '++ :' not in new_str:
                    new_str = re.sub(r':.*', ': getArg()', s)
                note_str = f'    note right : retrieved {num_args} parameters\n'
                lines[i] = new_str.rstrip() + '\n' + note_str
                changed = True
    if changed:
        with open(p, 'w', encoding='utf-8') as f: f.writelines(lines)
        print(f'Fixed getArg in {p}')

for path in glob.glob('docs/diagrams/**/*.puml', recursive=True): fix(path)
