import os
import shutil

template = '<script>window.location.href="{}";</script>'
template_iframe = '<meta name="viewport" content="width=device-width, initial-scale=1.0"><iframe src="{}" frameborder="0" style="width:100%;height:100%;"></iframe>'
with open('./_/config.txt', encoding='utf-8') as f:
    rules = [r.strip() for r in f.readlines() if r.strip() and not r.startswith('#')]

ignore = ['_', '.github', '.git']
dirs = [dir for dir in os.listdir('.') if not dir in ignore and os.path.isdir(dir)]
for dir in dirs:
    shutil.rmtree(dir, ignore_errors=True)

for rule in rules:
    code, url, *rest = rule.split(',')
    tpl = template
    if rest and rest[0].strip() == 'iframe':
        tpl = template_iframe

    if os.path.exists(code):
        continue
    os.makedirs(code)
    with open(os.path.join(code, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(tpl.format(url))