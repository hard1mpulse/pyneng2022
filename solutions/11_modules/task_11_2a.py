#!/usr/bin/env python3
from task_11_2 import create_network_map
from draw_network_graph import draw_topology 

def unique_network_map(topology_dict):
    duplicated_intfs=[]
    for intf in topology_dict.keys():
        if intf in topology_dict.values() and not topology_dict[intf] in duplicated_intfs:
            duplicated_intfs.append(intf)
    for intf in duplicated_intfs:
        del topology_dict[intf]
    return topology_dict


infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

draw_topology(unique_network_map(create_network_map(infiles)))