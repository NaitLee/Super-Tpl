class Converter {
    constructor() {
        this.fileInput = document.querySelector('input[type="file"]');
        this.button = document.querySelector('button');
        this.button.addEventListener('click', this.convert.bind(this));
    }
    convert() {
        class FileStatics {
            constructor(file) {
                this.sectionName = decodeURIComponent(file.name.split('.').slice(0, -1).join('.').slice(1));
                this.fileType = file.name.split('.').slice(-1)[0];
            }
        }
        let files = this.fileInput.files;
        let result = '';
        for (let i in files) {
            let file = files[i];
            let fileStatics = new FileStatics(file);
            let reader = new FileReader();
            reader.onload = event => {
                let content = event.target.result;
                switch (fileStatics.fileType) {
                    case 'ts':
                        content = window.ts.transpile(content);
                        break;
                }
                result += `\n[${fileStatics.sectionName}]\n${content}\n`;
                if (i == files.length - 1) {
                    let blob = new Blob([result]);
                    let a = document.createElement('a');
                    a.href = URL.createObjectURL(blob);
                    a.download = Math.random() + '.tpl';
                    a.click();
                }
            }
            reader.readAsText(file);
        }
    }
}
window.converter = new Converter();
