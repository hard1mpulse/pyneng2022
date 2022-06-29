#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
error_msg='Wrong IP!'


ip_corr=False
while not ip_corr:
    ip_str=input('Enter IP address: ')
    ip=[]
    if not len(ip_str.split('.')) == 4:
        print(error_msg)
        ip_corr=False
    else:
        for i in ip_str.split('.'):
            try:
                int(i)
            except ValueError:
                print(error_msg)
                ip_corr=False
                break
            if int(i) > 255 or int(i) < 0:
                print(error_msg)
                ip_corr=False
                break
            else:
                ip.append(int(i))
                ip_corr=True      
if not ip_corr:
    pass
else:      
    if ip[0] >= 1 and ip[0] <= 223:
        print('unicast')
    elif ip[0] >=224 and ip[0]<=239:
        print('multicast')
    elif ip_str == '255.255.255.255':
        print('local broadcast')
    elif ip_str == '0.0.0.0':
        print('unassigned')
    elif ip_corr:
        print('unused')
    else:
        pass