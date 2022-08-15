#!/usr/bin/env python3
def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    result={}
    with open(config_filename,'r') as f:
        l1cmd=''
        for line in f:
            if line.startswith('!') or ignore_command(line,ignore) or line=='\n' or line=='end\n':
                pass
            elif not line.startswith(' '):
                result.update({line.strip(): []})
                l1cmd=line.strip()
            elif line.startswith(' '):
                a=result.get(l1cmd)
                a.append(line.strip())
                result.update({l1cmd: a})
    return(result)
ignore = ["duplex", "alias", "Current configuration"]


b=convert_config_to_dict('config_sw1.txt')
print(b)