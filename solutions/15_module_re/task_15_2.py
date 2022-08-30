#!/usr/bin/env python3
import re
def parse_sh_ip_int_br(cmd_filename):
    result=[]
    f=open(cmd_filename)
    result = [match.groups() for match in re.finditer(r'(\S+) +([\d.]+|unassigned) +\w+ +\w+ +(up|down|administratively down) +(up|down)', f.read())]
    f.close()
    return result

if __name__ == "__main__":
    print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
