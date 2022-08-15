#!/usr/bin/env python3
def generate_access_config(intf_vlan_mapping, trunk_template):
  result=[]
  for intf in intf_vlan_mapping.keys():
    result.append('interface '+intf)
    vlans_str_list=[]
    for vlan in intf_vlan_mapping.get(intf):
      vlans_str_list.append(str(vlan))
    for cfg_line in trunk_template:
      if not "allowed" in cfg_line:
        result.append(cfg_line)
      else:
        result.append(cfg_line+' '+','.join(vlans_str_list))
  return result    



trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

t1=generate_access_config(trunk_config,trunk_mode_template)
t2=generate_access_config(trunk_config_2,trunk_mode_template)
print(t1)
print(t2)