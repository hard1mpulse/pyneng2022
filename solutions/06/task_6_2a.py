#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

error_msg='Wrong IP!'
ip_str=input('Enter IP address: ')

ip=[]
ip_corr=True
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
      else:
         ip.append(int(i))

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