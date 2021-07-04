import os, sys, urllib.parse, base64

def convert(dirname = './'):
    folder = os.path.abspath(dirname)

    files = filter(lambda x: os.path.isfile(folder + '/' + x) and x.startswith('~'), os.listdir(folder))

    template = []

    for i in files:
        f = open(folder + '/' + i, 'r', encoding='utf-8')
        content = f.read()
        f.close()
        if i.endswith('.ts'):
            g = open('.temp.ts', 'w', encoding='utf-8')
            g.write(content)
            g.close()
            code = os.system('node -e "const ts = require(\'./typescriptServices\'); const fs = require(\'fs\'); fs.readFile(\'.temp.ts\', \'utf8\', (err, data) => { console.log(ts.transpile(data)); });" > .temp.js')
            if code != 0:
                print('\n * Error on ts to js convert: exit code (%i)' % code)
                continue
            f = open('.temp.js', 'r', encoding='utf-8')
            js = f.read()
            f.close()
            os.remove('.temp.ts')
            os.remove('.temp.js')
            content = js
        section = '.'.join(urllib.parse.unquote(i).split('.')[0:-1])[1:]
        template.append(f'\n[{section}]\n{content}\n')

    result = ''.join(template)

    f = open('output.tpl', 'w', encoding='utf-8')
    f.write(result)
    f.close()

if __name__ == '__main__':
    convert(sys.argv[1])
