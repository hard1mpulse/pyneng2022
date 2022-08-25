#!/usr/bin/env python3
import re
def get_ip_from_cfg(cfg_filename):
    result={}
    with open(cfg_filename) as f:
        intf_found=False
        for line in f:
            if line.startswith('interface '):
                intf_found=True
                intfname=line.split()[-1]
            if intf_found and re.match(r'\ ip address \d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+',line):
                ipconfig=re.match(r'\ ip address \d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+',line).group()
                result.update({intfname: (ipconfig.split()[-2],ipconfig.split()[-1])})
                intf_found=False
    return result

if __name__ == "__main__":
    print(get_ip_from_cfg('config_r1.txt'))