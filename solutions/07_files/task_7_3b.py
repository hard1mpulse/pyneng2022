#!/usr/bin/env python3
mac_out_temp='{:8} {:15} {:8}'
fdb_list=[]
req_vlan=input('Enter VLAN ID: ')
with open('CAM_table.txt','r') as f:
    for line in f:
        if '.' in line:
            line_list=line.split()
            fdb_list.append([line_list[0],line_list[1],line_list[3]])
for fdb_line in fdb_list:
    if fdb_line[0] == req_vlan:
        print(mac_out_temp.format(fdb_line[0],fdb_line[1],fdb_line[2]))
