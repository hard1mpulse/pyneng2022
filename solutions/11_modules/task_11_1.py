#!/usr/bin/env python3
def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result={}
    for line in command_output.split('\n'):
        if 'show cdp neighbors' in line:
            devname=line.split('>')[0]
        elif ' Fa ' in line or ' Eth' in line:
            neigbor_id=line.split()[0]
            local_int=line.split()[1]+line.split()[2]
            remote_int=line.split()[-2]+line.split()[-1]
            result.update({(devname,local_int):(neigbor_id,remote_int)})
    return result

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))