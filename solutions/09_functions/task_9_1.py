#!/usr/bin/env python3

def generate_access_config(intf_vlan_mapping, access_template):
    result=[]
    for intf in intf_vlan_mapping.keys():
        result.append('interface {}'.format(intf))
        for cfg_line in access_mode_template:
            if not "vlan" in cfg_line:
                result.append(cfg_line)
            else:
                result.append(cfg_line+' '+str(intf_vlan_mapping.get(intf)))
    return result
access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}


