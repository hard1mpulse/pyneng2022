#!/usr/bin/env python3

route_temp='''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
'''

with open('ospf.txt','r') as f:
    for line in f:
        route_list=line.split()
        print(route_temp.format(route_list[1],route_list[2].strip('[]'),route_list[4].rstrip(','),route_list[5].rstrip(','),route_list[6]))