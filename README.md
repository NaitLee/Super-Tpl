# Super-Tpl
*Make managing work of HFS templates easier.*

## Usage
By parting template sections into independent files, creation of a template will be structured.

A valid file must be like: `~special%3Astrings%7Ccache.txt`

That is, start with `~`, URIEncode special characters, also with a extension.

Besides, TypeScript is also supported. Just name a `.ts` file, then it will be transpiled to JavaScript.

### index.html
This is web interface of super-tpl. drag all parts to the file input, click `OK`, then you got template downloaded.

Useful for simple testing and building.

If TypeScript is used, be sure do not miss file `typescriptServices.js`.

### converter.py
This is Python3 version of super-tpl. by running command `python3 converter.py folder_of_parts`, the process is done.

Useful for workspace, that need change files frequently.

If TypeScript is used, be sure to have Node.js installed (or on Windows, `node.exe` put inside folder of converter.py), also `typescriptServices.js` is there.
