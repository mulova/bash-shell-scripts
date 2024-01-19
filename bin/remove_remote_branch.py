#!/usr/bin/env python3
import os
import sys
import subprocess

prefix='origin/'
regex=sys.argv[1]
cmd=f"git branch -r | grep -E '{regex}'"
branches=subprocess.check_output(cmd, shell=True, text=True).split(' ')
for b in branches:
    if b.startswith(prefix):
        branch=b[len(prefix):]
        print(f'removing branch {b}')
        os.system(f'git push origin -d {branch}')

