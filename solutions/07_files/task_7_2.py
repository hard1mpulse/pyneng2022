#!/usr/bin/env python3
from sys import argv
conf_file= argv[1]

with open(conf_file,'r') as f:
    for line in f:
        if line.startswith('!'):
            pass
        else:
            print(line.strip())
