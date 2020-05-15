import re
import operator
from ip_generator import gen_ip
"""Разобрать пример с поиском ipv4 адреса
Пройтись по файлу с ipv4 адресами и проверить, что в каждой строке 
содержится корректный ip адрес. Если есть некорректный, то распечатать его. 
Конечная цель проверить количество найденных адресов и количество строк в файле
"""
def ip4():
    ip4 = re.compile(r"""
                    (?:(?:25[0-5]           # 250-255
                    |2[0-4][0-9]            # 200-249
                    |[1]?[0-9]?[0-9])\.){3} # 0-199 3 октета
                    (?:25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])""", re.VERBOSE) # последний октет
    FILENAME = "apache.log.txt"
    count = 0
    s = ' '
    with open (FILENAME, "r") as f:
        while s != '':
            s = f.readline()                    # Считывание файла в строку
            if ip4.match(s) is not None:        # Применить регулярку
                count += 1
    print(count)
# -----------------------------------------------------------------------------
def string_pazle():
    """
    Дана строка 'aba accca azzza wwwwa'.
    Напишите регулярку, которая найдет все
    слова по краям которых стоят буквы 'a', и заменит
    каждую из них на '!'. Между буквами a может быть любой символ (кроме a).
    """
    string = "aba accca azzza wwwwa"
    str_parse = re.compile(r"""
                    \ba[^a]*a\b # Все слова с а и до а
                    """, re.VERBOSE)
    def func(x):
        x[0] = '!'
        x[-1] = '!'
    result = str_parse.sub(lambda x: f'!{x.group()[1:-1]}!',string)
    print(result)

def HTML_parse():
    """
    Дан текст вперемешку HTML тегами,
    ваша задача очистить его от всех тегов с помощью
    регулярных выражений list_ = [
        '<strong>Наши</strong> <em>ховерборды</em> лучшие в <u>мире</u>!',
        '<EM>Световой меч</EM> в <strong>каждый</strong> дом!'
        ];
    Вернуть единую строку без тегов, полученную
    после их удаления. С сохранением построчного форматирования
    ```Наши ховерборды лучшие в мире !',
       Световой меч в каждый дом!```
    """
    list_ = [
            '<strong>Наши</strong> <em>ховерборды</em> лучшие в <u>мире</u>!',
            '<EM>Световой меч</EM> в <strong>каждый</strong> дом!'
            ]
    html_parse = re.compile(r"""
                            <.*?>
                            """, re.VERBOSE)
    result = ''
    for item in list_:
        result += html_parse.sub('',item)
        result += '\n'
    print(result)

def math_parse():
    """
    С помощью регулярных выражений сделать парсер
    строк и проверить корректность следующих выражений:
    """
    string = """
    1 + 10 = 11
    20 - 12 = 8
    7.5 / 2.5 = 3
    3 * 0.5 = 1.5
    0.05 + 6 = 6.05
    """
    oper = {"+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.floordiv}
    math_parser = re.compile(r"(\d+(?:\.\d+)?)\ ([+\-*\/])\ (\d+(?:\.\d+)?)\ =\ (\d+(?:\.\d+)?)", re.VERBOSE)
    for item in math_parser.finditer(string):
        result = item.groups()
        print(result)
        print(oper[result[1]](float(result[0]),float(result[2])) == float(result[3]))

def gen_ip_re():
    """Генератор, который генерирует любые ip адреса,
    сделать декоратор, который будет выдавать адреса только по указанному шаблону.
    Шаблон статично прописывается в декораторе
    Доступны следующие форматы:
    10.X.X.X
    192.168.[0-31, 128-191].X,
    """
    gen = gen_ip([[], [], [], []])
    for i in range(20):
        print(next(gen))

def main():
    # ip4()
    # string_pazle()
    # HTML_parse()
    # math_parse()
    gen_ip_re()
if __name__ == '__main__':
    main()


