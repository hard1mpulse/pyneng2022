#!/usr/bin/env python3
from task_12_1 import ping_ip,ping_ip_addresses
import ipaddress

def convert_ranges_to_ip_list(ip_list):
    result=[]
    for addr in ip_list:
        is_range=False
        try:
            result.append(str(ipaddress.ip_address(addr)))
        except ValueError:
            is_range=True
        if is_range:
            try:
                ip_max=ipaddress.ip_address(addr.split('-')[-1])
                ip_min=ipaddress.ip_address(addr.split('-')[0])
                while not ip_min > ip_max:
                    result.append(str(ip_min))
                    ip_min=ip_min+1
            except ValueError:
                ip_min=ipaddress.ip_address(addr.split('-')[0])
                while int(str(ip_min).split('.')[-1]) <= int(addr.split('-')[-1]):
                    result.append(str(ip_min))
                    ip_min=ip_min+1
    return result


if __name__ == "__main__":
    print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))
