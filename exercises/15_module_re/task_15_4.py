# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re
from pprint import pprint

def get_ints_without_description(filename):
    """
    Функция обрабатывает конфигурацию и возвращать список имен интерфейсов,
    на которых нет описания (команды description).

    filename - имя файла, в котором находится конфигурация устройства
    """
    result = []
    regex = (
        r"\ninterface (?P<intf>\S+)\n" # Interface
        r"(?: description (?P<desc>.+)\n)?"
        r" \w+ .+\n"
    )

    with open(filename) as f:
        match_all = re.finditer(regex, f.read())
        for match in match_all:
            intf, desc = match.group("intf", "desc")
            if not match.lastgroup == "desc":
                result.append(intf)

    return result


if __name__ == "__main__":
    output = get_ints_without_description("config_r1.txt")
    pprint(output)
