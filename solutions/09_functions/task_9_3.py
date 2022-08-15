#!/usr/bin/env python3
def get_int_vlan_map(config_filename):
    access_ports={}
    trunk_ports={}
    res_tuple=(access_ports,trunk_ports)
    with open(config_filename) as f:
        interface_found=False
        for line in f:
            if line.startswith('interface FastEthernet'):
                interface_found=True
                interface_name=line.split()[-1]
            elif 'access vlan' in line and interface_found :
                access_ports.update({interface_name: int(line.split()[-1])})
            elif 'allowed vlan' in line and interface_found:
                vlan_list=[]
                for vlan in line.split()[-1].split(','):
                    vlan_list.append(int(vlan))
                trunk_ports.update({interface_name: vlan_list})
            elif interface_found and line.startswith('!'):
                interface_found=False
    return res_tuple

print(get_int_vlan_map('config_sw1.txt'))