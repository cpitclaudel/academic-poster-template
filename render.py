#!/usr/bin/env python3
# Copyright © 2020 Clément Pit-Claudel
# https://github.com/cpitclaudel/academic-poster-template
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Render a jinja2 template."""

import argparse
from os.path import dirname, realpath, relpath

from jinja2 import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='Render a Jinja2 template.')
    parser.add_argument("input", help="Read from INPUT")
    parser.add_argument("output", nargs="?", default="-",
                        help="Write to OUTPUT (default: -)")
    return parser.parse_args()

def main():
    args = parse_arguments()
    srcdir = '.' #dirname(realpath(args.input))
    env = Environment(loader=FileSystemLoader(srcdir),
                      autoescape=select_autoescape(('html', 'xml')),
                      trim_blocks=True,
                      undefined=StrictUndefined)
    with argparse.FileType('w')(args.output) as output:
        output.write(env.get_template(relpath(args.input, srcdir)).render())

if __name__ == '__main__':
    main()
