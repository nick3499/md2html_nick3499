#!/usr/bin/env python
'''Convert MD to HTML.'''
from webbrowser import open as wb_open
from markdown import markdownFromFile


def convert():
    '''Convert MD to HTML from MD file.'''
    markdownFromFile(
        input='example_readme.md',
        output='example_readme.html',
        encoding='utf8',
        extensions=['fenced_code'])
    wb_open('http://localhost:8000/example_readme.html')


if __name__ == '__main__':
    convert()
