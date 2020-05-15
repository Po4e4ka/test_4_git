from numpy import random
import re

def fab_dec_gen_ip(ip_patter):
    def dec_gen_ip(func):
        def wrapper(*args):
            local_gen = func(*args)
            ip_pattern = re.compile(ip_patter)
            for result in local_gen:
                if ip_pattern.search(result):
                    yield result
        return wrapper
    return dec_gen_ip
@fab_dec_gen_ip(r"1[0-9][0-9]\.168(?:\.\d{1,3}){2}")
def gen_ip(tempale):
    """
    По шаблону:
	[[],[],[],[]] Числа, случайным образом из представленного списка
	Если пустой, то из всего доступного диапазона
    Просто набор чисел [23, 24, 145, …]
    Строка «100-120»
    Кортеж (150-220)
    * придумать формат где левая или правая граница могут быть опущены,
    тогда считается от начала или конца соответственно “[:200]” -> [0, 200]  (100:) -> [100:255]

    Перезапуск шаблона через корутину

    Работа с файлами:
    Запись сгенерированных ip адресов в файл
    Функция для считывания шаблона из json (формат придумываете сами)
    * Декоратор для записи в файл


    Через аргументы сделать передачу следующих аргументов
    * Шаблона. 4 отдельных позиционных аргумента для задания шаблона. Каждый аргумент не обязательный
    Количество ip адресов (именованный аргумент)
    Флаг для вывода в консоль
    Флага записи адресов в файл. Если флаг установлен, то должен запрашиваться
    название файла вывода. В данном случае вывод в консоль не должен производиться
    * Необязательный аргумент, для считывания шаблона из файла

    :return:
    """
    while True:
        ip_list = []
        for i in tempale:
            if type(i) is str:
                if '-' in i:
                    i = i.split('-')
                    ip_list.append(range(int(i[0]), int(i[1]) + 1))
                elif ':' in i:
                    i = i.split(':')
                    if i[0] == '':
                        i[0] = '0'
                    if i[1] == '':
                        i[1] = '256'
                    ip_list.append(range(int(i[0]), int(i[1])))
            elif type(i) is tuple:
                ip_list.append(range(i[0],i[1]+1))
            elif i == []:
                ip_list.append(range(0,256))
                continue
            elif i:
                ip_list.append([i])

            else:
                ip_list.append(range(256))


        _input = yield '.'.join(map(str,map(random.choice,ip_list)))
        if _input is not None:
            tempale = _input

