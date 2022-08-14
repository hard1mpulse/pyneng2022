#!/usr/bin/env python3
from sys import argv
conf_file= argv[1]
res_file= argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(conf_file,'r') as conf, open(res_file,'w') as res:
    for line in conf:
        line_valid=True
        if line.startswith('!'):
            line_valid=False
            pass
        else:
            for stopword in ignore:
                if stopword in line:
                    line_valid=False
                    break
        if line_valid:
            res.write(line)
