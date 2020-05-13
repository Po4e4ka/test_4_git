import argparse
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
    parser.add_argument("-c",
                        "--count",
                        type=int,
                        default=5,
                        help="Счетчки вызова генератора")
    subparsers = parser.add_subparsers(dest="command")

    create_subparser_save(subparsers)
    create_subparser_show(subparsers)

    return parser