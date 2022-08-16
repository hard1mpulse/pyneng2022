#!/usr/bin/env python3
from task_12_1 import ping_ip,ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list
import ipaddress
from tabulate import tabulate

def print_ip_table(avail_ip,unavail_ip):
    print(tabulate({'Reachable': avail_ip, 'Unreachable': unavail_ip}, headers='keys'))



if __name__ == "__main__":
    a=ping_ip_addresses(convert_ranges_to_ip_list(['172.16.172.230-254']))
    print_ip_table(a[0],a[1])

