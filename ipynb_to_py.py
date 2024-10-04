
'''
jupyter nbconvert --to python file1 --output file2
'''

import os
from pathlib import Path
import subprocess as sp


src = Path('DUDL_PythonCode')
dst = Path('PythonCode')


def new_path(item, dst):
    name = item.name
    new_name = name.removeprefix('DUDL_').removesuffix('.ipynb')
    return dst / new_name


def nbconvert(file1, file2):
    file2.parent.mkdir(parents=True, exist_ok=True)
    sp.run(['jupyter', 'nbconvert', '--to', 'python', str(file1),
        '--output-dir', str(file2.parent),
        '--output', file2.name])


def process_directory(src, dst, f):
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_file():
            outpath = new_path(item, dst)
            f(item, outpath)
        elif item.is_dir():
            new_output_dir = dst / item.name
            process_directory(item, new_output_dir, f)


process_directory(src, dst, nbconvert)
