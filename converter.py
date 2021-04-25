import os, sys, urllib.parse, base64

folder = os.path.abspath(sys.argv[1])

files =filter(lambda x: os.path.isfile(folder + '/' + x) and x.startswith('~'), os.listdir(folder))

template = []

for i in files:
    f = open(folder + '/' + i, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    if i.endswith('.ts'):
        b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        os.system(f'node -e "let ts = require(\'./typescriptServices\'); console.log(ts.transpile(Buffer.from(\'{b64}\', \'base64\').toString(\'utf8\')));">.temp.js')
        f = open('.temp.js', 'r', encoding='utf-8')
        js = f.read()
        f.close()
        os.remove('.temp.js')
        content = js
    section = '.'.join(urllib.parse.unquote(i).split('.')[0:-1])[1:]
    template.append(f'\n[{section}]\n{content}\n')

result = ''.join(template)

f = open('output.tpl', 'w', encoding='utf-8')
f.write(result)
f.close()
