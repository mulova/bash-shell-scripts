#!/usr/bin/env python3
import os
import sys
import subprocess

def add_branch(branch):
    hash_cmd=f"git ls-remote | grep '{branch}$'"
    print (hash_cmd)
    str=subprocess.check_output(hash_cmd, shell=True, text=True).split()
    add_tag_cmd=f"git tag t/{branch} {str[0]}"
    print(add_tag_cmd)
    r1=subprocess.check_output(add_tag_cmd, shell=True, text=True)
    push_tag_cmd=f"git push origin t/{branch}"
    print(push_tag_cmd)
    r2=subprocess.check_output(push_tag_cmd, shell=True, text=True)

prefix='origin/'
regex=sys.argv[1]
branch_list_cmd=f"git branch -r | grep -E '{regex}'"
branches=subprocess.check_output(branch_list_cmd, shell=True, text=True).split(' ')
for b in branches:
    if b.startswith(prefix) and not b.startswith(prefix+'t/'):
        branch=b[len(prefix):].strip()
        add_branch(branch)
        os.system(f'git push origin -d {branch}')

