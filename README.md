# Super-Tpl
*Make managing work of HFS templates easier.*

## Usage
By parting template sections into independent files, creation of a template will be structured.

A valid file must be like: `~special%3Astrings%7Ccache.txt`

That is, start with `~`, URIEncode special characters, also with a extension.

Besides, TypeScript is also supported. Just name a `.ts` file, then it will be transpiled to JavaScript.
