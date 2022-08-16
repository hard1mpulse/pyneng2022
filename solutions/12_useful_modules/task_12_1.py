#!/usr/bin/env python3
import subprocess

def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False

def ping_ip_addresses(ip_list):    
    avail_ip=[]
    unavail_ip=[]
    for ip in ip_list:
        if ping_ip(ip):
            avail_ip.append(ip)
        else:
            unavail_ip.append(ip)
    return (avail_ip,unavail_ip)

if __name__ == "__main__":
    ip_addr=['192.168.0.1','8.8.8.8','172.16.200.1']
    print(ping_ip_addresses(ip_addr))