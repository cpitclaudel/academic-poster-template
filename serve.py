#!/usr/bin/env python

from livereload import Server, shell

if __name__ == "__main__":
    server = Server()
    server.watch('poster.jinja2', shell('make'))
    server.watch('poster.less', shell('make'))
    server.watch('docs/*.jinja2', shell('make'))
    server.watch('docs/**/*.png')
    server.watch('docs/**/*.svg')
    server.serve()
