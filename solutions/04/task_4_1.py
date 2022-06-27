#!/usr/bin/env python

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

print(nat.replace ('FastEthernet', 'GigabitEthernet'))