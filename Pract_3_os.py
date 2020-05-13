import os
import argparse
"""
name (uname) – получение имени (информации) операционной системы
environ – получение словаря переменных окружения
listdir – получение списка файлов и директорий в папке
mkdir (makedirs) /rmdir – создание и удаление папок
rename – переименование файла или папки
access – проверяет наличие доступа текущего пользователя к указанному месту. Флаги: os.F_OK, R_OK, W_OK, X_OK
"""
# access_list = [os.F_OK, os.R_OK, os.W_OK, os.X_OK]
# for i in access_list:
#     print(os.access('test.txt', i))


def lol():
    """
    Напишите приложение, которое считывает переменные окружения
    и в отформатированном виде выводит их и их значение в консоль,
    если среди этих аргументов присутствует “PY_DEBUG”,
    значение которого равно ‘True’ (иначе – ничего не делает)
    """
    os.environ['PY_DEBUG'] = "True"
    if 'PY_DEBUG' in os.environ and os.environ['PY_DEBUG'] == "True":
        for name, value in os.environ.items():
            print(f"{name} : {value}")

def lol_1(start=1, step=1):
    """
    Реализовать программу, которая вычисляет целиком ряд арифметической прогрессии.
    Программа должна реализовывать следующую логику:
        При запуске необходим указать аргументы, отвечающие за начальное значение
    (именованные или позиционные – на ваш выбор) и за шаг прогрессии,
    далее должен идти флаг save/show
            При запуске с флагом ‘save’ далее должен идти параметр –i,
        который указывает путь до файла, в который необходимо сохранить
        итоговый вычисленный ряд. Проверяйте возможность сохранения.
            При запуске с флагом ‘show’ далее не должно идти никакого параметра
        и вычисленный ряд выводится в консоль
    """
    n = start
    while True:
        _input = yield n
        if _input is not None:
            n = _input
        else:
            n += step

def main():
    parser = create_parser()
    namespace = parser.parse_args()
    print(namespace)
    COUNT = 5
    if namespace.command == 'show':
        gen = lol_1(namespace.start, namespace.step)
        for _ in range(COUNT):
            print(next(gen))
    elif namespace.command == 'save':
        with open(namespace.output_file, 'w') as f:
            gen = lol_1(namespace.start, namespace.step)
            for _ in range(COUNT):
                f.write(str(next(gen)))
                f.write('\n')


def create_subparser_show(subparsers):
    subparsers.add_parser("show",
                          help="Режим вывода информации в консоль")

def create_subparser_save(subparsers):
    save_subparsers = subparsers.add_parser("save",
                                            help="Режим сохранения в файл")
    save_subparsers.add_argument('-i',
                                 required=True,
                                 type=str,
                                 dest='output_file',
                                 help="Файл для вывода")

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("start",
                        type=int,
                        help="Начальное значение арифметической прогрессии")
    parser.add_argument("step",
                        type=int,
                        help="Шаг арифметической прогрессии")
    subparsers = parser.add_subparsers(dest="command")
    create_subparser_save(subparsers)
    create_subparser_show(subparsers)


    return parser

if __name__ == "__main__":
    try:
        main()
    except:
        exit()
