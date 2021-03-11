# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(ip_range):
    for i in ip_range:
        if "-" in i:
            ip_range_dashed = i.split("-")
            ip_main = ".".join(ip_range_dashed[0].split(".")[0:3])
            if "." in ip_range_dashed[1]:
                ip_start = ip_range_dashed[0].split(".")[-1]
                ip_stop = ip_range_dashed[1].split(".")[-1]
                list_of_ips = [
                    "{}.{}".format(ip_main, last_octet)
                    for last_octet in range(int(ip_start), int(ip_stop) + 1)
                ]
            elif "." not in ip_range_dashed[1]:
                ip_start = ip_range_dashed[0].split(".")[-1]
                ip_stop = ip_range_dashed[1]
                list_of_ips = [
                    "{}.{}".format(ip_main, last_octet)
                    for last_octet in range(int(ip_start), int(ip_stop) + 1)
                ]
        else:
            list_of_ips = [ip_range]
    return list_of_ips
 
if __name__ == '__main__':
    test = ["8.8.4.4", "1.1.1.1-3", "172.21.41.128-172.21.41.132"]
    result = convert_ranges_to_ip_list(test)
    print(result)
