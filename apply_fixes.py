import os, glob, re

def process_file(p):
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # 1. Replace multi getArgs
    # We find things like:   obj -> cmd ++ : getArg("x"), getArg("y")
    # Replace with:          obj -> cmd ++ : getArg()
    #                        note right : retrieved N parameters
    
    def repl_getarg(match):
        prefix = match.group(1) # e.g. "handler -> cmd "
        act = match.group(2)    # e.g. "++ "
        call = match.group(3)   # e.g. "getArg(\"n\"), getArg(\"d\")"
        
        num_args = call.count('getArg')
        # if only 1, don't change
        if num_args <= 1:
            return match.group(0)
            
        res = f'{prefix}{act}: getArg()\n    note right : retrieved {num_args} parameters'
        return res

    content = re.sub(r'^(.*?)(\+\+\s+|)(:\s*getArg\([^)]*\)(?:,\s*getArg\([^)]*\))+.*)$', repl_getarg, content, flags=re.MULTILINE)

    # 2. Replace alt with opt if there's no else
    # Since regex is hard for nested, we use a simple state machine per lines
    lines = content.split('\n')
    new_lines = []
    
    for i in range(len(lines)):
        s = lines[i]
        if s.lstrip().startswith('alt '):
            # check the block
            depth = 1
            has_else = False
            is_valid = True
            for j in range(i+1, len(lines)):
                ts = lines[j].strip()
                if ts.startswith('alt ') or ts.startswith('opt ') or ts.startswith('loop '):
                    depth += 1
                elif ts == 'end':
                    depth -= 1
                    if depth == 0:
                        break
                elif (ts.startswith('else ') or ts == 'else'):
                    if depth == 1:
                         has_else = True
            
            # if we found no else, we can safely change this 'alt ' to 'opt '
            if not has_else:
                lines[i] = s.replace('alt ', 'opt ', 1)

    content = '\n'.join(lines)

    if original != content:
        print(f"Fixed {p}")
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)

for path in glob.glob('docs/diagrams/**/*.puml', recursive=True):
    process_file(path)
