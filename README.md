# md2html_nick3499
Convert MD to HTML using Markdown along with web browser display

### Python, markdown.markdownFromFile, webbrowser

### Virtual Environment

A Python virtual environment was originally used to develop this app. Basically, to make the `markdown` available.

```
Markdown==3.3.3
```

### Start the App

To run the app, enter the following in a Unix-like terminal emulator:

```
$ ./start.sh
```

Note: permissions may need to be adjusted.

### Shebang Line

```
#!/usr/bin/env python
```

```
>>> hex(ord('#'))
'0x23'
>>> hex(ord('!'))
'0x21'
```

In a Unix-like OS, a **shebang** can be used with a Python executable text file (.py). The human-readable shebang or `#!`, is encoded to ASCII '0x23 0x21' which becomes the instance of a 'magic number'. The shebang is detected by the `env` function.

### Module Documentation

```
>>> __doc__
'Convert MD to HTML.'
```

In the Python interactive browser, `__doc__` accesses the module's documentation.

### Module Imports

```python
from webbrowser import open as wb_open
from markdown import markdownFromFile
```

Both the `webbrowser.open()` and `markdown.markdownFromFile()` are imported.

### Function Definition

```python
def convert():
```

The keyword `def` begins the function defintion which defines `convert()` and adds it to the namespace.

### Function Documentation

```
'''Convert MD to HTML from MD file.'''
```

```
>>> convert.__doc__
'Convert MD to HTML from MD file.'
```

In the Python interactive browser, `convert.__doc__` accesses the function's documentation.

### markdown.markdownFromFile()

```python
markdownFromFile(
    input='example_readme.md',
    output='example_readme.html',
    encoding='utf8',
    extensions=['fenced_code'])
```

The shortcut function `markdownFromFile()` initializes an instance of Markdown and calls `convertFile()` instead of `convert`.
The four API keys `input`, `output`, `encoding` and `extensions` are exposed in code above. The markdown code in `example_readme.md` is written to a file.

The `extensions` key was included to make fenced code display as it should. For example, to make it display as pre-formatted text.

### webbrowser.open()

```python
wb_open('http://localhost:8000/example_readme.html')
```

Finally, `webbrowser.open()` displays the HTML code.
