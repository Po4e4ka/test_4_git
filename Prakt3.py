import json
import pickle
def zad_1(filename):
    """
    Задание: используя только Python, создать файл с любым названием, записать туда результат
    пользовательского ввода, затем закрыть файл. После этого открыть в бинарном виде и вывести
    в консоль бинарное представление данного ввода.
    :param line:
    :return:
    """
    while True:
        stri = input()
        with open(filename, 'a') as f:
            f.write(stri)
            f.write('\n')
def zad_1_readbinary(filename):
    """
    После этого открыть в бинарном виде и вывести
    в консоль бинарное представление данного ввода.
    :param filename:
    :return:
    """
    with open(filename, 'rb') as f:
        print(f.read())
def zad_2(object, filename):
    """
    Задача: создать сложную структуру (словарь, у которого есть внутри словарь и список),
    сериализовать ее в формат json и сохранить в файл.
    """
    with open(filename, 'w') as f:
        json.dump(object, f, indent=4)
def zad_2_2(filename):
    """
    Результат открыть текстовым редактором и посмотреть на предмет понятности.
    """
    with open(filename, 'r') as f:
        print(json.load(f))
def zad_3(objec, filename):
    """
    Задача: создать сложную структуру (словарь, у которого есть внутри словарь и список), сериализовать ее с помощью pickle и сохранить в файл.
    Не забудьте, что файл открывается в бинарном режиме.
    """
    with open(filename, 'wb') as f:
        pickle.dump(objec, f)
def zad_3_3(filename):
    """
    Результат открыть текстовым редактором и посмотреть на предмет понятности.
    """
    with open(filename, 'rb') as f:
        print(pickle.load(f))

FILENAME = 'test.txt'
def main():
    # zad_1(FILENAME)
    # zad_1_readbinary(FILENAME)
    dict_1 = {'gkl':345, 7:'lol', 456:('15',15)}
    # zad_2(dict_1,FILENAME)
    # zad_2_2(FILENAME)
    zad_3(dict_1, FILENAME)
    zad_3_3(FILENAME)




if __name__ == "__main__":
    main()