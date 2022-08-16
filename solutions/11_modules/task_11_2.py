#!/usr/bin/env python3
from task_11_1 import parse_cdp_neighbors

def create_network_map(filenames):
    topo={}
    for f in filenames:
        with open(f) as cdpn:
            topo.update(parse_cdp_neighbors(cdpn.read()))
    return topo

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

if __name__ == "__main__":
    print(create_network_map(infiles))
