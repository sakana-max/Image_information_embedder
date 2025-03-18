import os

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    if lines[0] == "jp":
        return "jp"
    else:
        return "en"

# 書き込みプログラム
def write_file(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)
