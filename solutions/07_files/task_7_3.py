#!/usr/bin/env python3
mac_out_temp='{:8} {:15} {:8}'
with open('CAM_table.txt','r') as f:
    for line in f:
        if '.' in line:
            line_list=line.split()
            print(mac_out_temp.format(line_list[0],line_list[1],line_list[3]))