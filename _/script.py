import os
import shutil

template = '<script>window.location.href="{}";</script>'
with open('./_/config.txt', encoding='utf-8') as f:
    rules = [r.strip() for r in f.readlines() if r.strip() and not r.startswith('#')]

ignore = ['_', '.github']
dirs = [dir for dir in os.listdir('.') if not dir in ignore and os.path.isdir(dir)]
for dir in dirs:
    shutil.rmtree(dir, ignore_errors=True)

for rule in rules:
    code, url = rule.split(',')
    if os.path.exists(code):
        continue
    os.makedirs(code)
    with open(os.path.join(code, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(template.format(url))