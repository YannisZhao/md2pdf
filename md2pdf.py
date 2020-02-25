#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import getopt

filter = ['.md']

def show_usages():
    usage = '''
Usage:

    convert markdown file(s) to pdf file.

    -h, --help  print help message
    -d, --src-dir   the directory where markdown file(s) will load
    -i, --input-files  specify input markdown file(s) 
    -o, --output-file   specify the generated output pdf file
    '''
    print(usage)

def get_md_files(parent):

    md_files = []

    print("scan markdown files in", parent)

    for root, dirs, files in os.walk(parent):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.splitext(filepath)[1] in filter:
                md_files.append(os.path.join(root, filename))
            
    return sorted(md_files)

def convert(input_files, output_file):
    prepared_cmd = "pandoc -f markdown -t latex {} -o {}";
    cmd = prepared_cmd.format(" ".join(input_files), output_file);
    os.system(cmd)

if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hd:i:o:', ['help', 'src-dir=', 'input-files=', 'output-file='])
    except getopt.GetopError:
        show_usages()
        sys.exit(3)

    src_dir = None
    input_files = []
    output_file = None

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_usages()
            sys.exit(0)
        elif opt in ('-d', '--src-dir'):
            src_dir = arg
        elif opt in ('-i', '--input-files'):
            input_files.append(arg)
        elif opt in ('-o', '--output-file'):
            output_file = arg
        else:
            print('Unrecognized option ', opt)
            sys.exit(3)

    assert src_dir or input_files, 'please specify src directory or markdown file(s) via -d or -i'
    assert output_file, 'please specify output file via -o'

    if len(input_files) <= 0:
        input_files = get_md_files(src_dir);

    convert(input_files, output_file)

