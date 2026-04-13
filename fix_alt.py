import os
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
         lines = f.readlines()
         
    new_lines = []
    i = 0
    while i < len(lines):
         line = lines[i]
         if line.strip().startswith('alt '):
              # Look ahead to find 'end' and check if there's an 'else'
              has_else = False
              j = i + 1
              depth = 1
              end_idx = -1
              while j < len(lines):
                   tl = lines[j].strip()
                   if tl.startswith('alt ') or tl.startswith('opt ') or tl.startswith('loop '):
                       depth += 1
                   elif tl == 'end':
                       depth -= 1
                       if depth == 0:
                           end_idx = j
                           break
                   elif tl.startswith('else ') or tl == 'else':
                       if depth == 1:
                           has_else = True
                   j += 1
              
              if (not has_else and end_idx != -1):
                   lines[i] = lines[i].replace('alt ', 'opt ', 1)
         new_lines.append(lines[i])
         i += 1

    if ''.join(new_lines) != ''.join(lines):
         print(f'Fixed {filepath}')
         with open(filepath, 'w', encoding='utf-8') as f:
             f.writelines(new_lines)

for file in glob.glob('docs/diagrams/**/*.puml', recursive=True):
    fix_file(file)
