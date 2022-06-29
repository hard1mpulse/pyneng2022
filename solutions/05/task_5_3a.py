#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

conf_temp= dict(access='Enter VLAN: ',trunk='Enter VLANs: ')
int_type=(input('Enter interface mode (access/trunk): '))
interface=(input('Enter interface name: '))
vlans=(input(conf_temp[int_type]))
conf_temp.clear()
conf_temp= dict(access=access_template,trunk=trunk_template)
print('interface {}'.format(interface))
print('\n'.join(conf_temp[int_type]).format(vlans))
