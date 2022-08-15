#!/usr/bin/env python3

def generate_access_config(intf_vlan_mapping, access_template,psecurity=None):
    result=[]
    for intf in intf_vlan_mapping.keys():
        result.append('interface {}'.format(intf))
        for cfg_line in access_mode_template:
            if not "vlan" in cfg_line:
                result.append(cfg_line)
            else:
                result.append(cfg_line+' '+str(intf_vlan_mapping.get(intf)))
        if psecurity:
            result=result+psecurity
    return result


access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

cfg_not_psec=generate_access_config(access_config,access_mode_template)
print(cfg_not_psec)
cfg_psec=generate_access_config(access_config,access_mode_template,port_security_template)
print(cfg_psec)