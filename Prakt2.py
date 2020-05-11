import numpy as np
import datetime
def zad_1():
    """
    Создать список, в котором каждый элемент – кортеж из двух чисел.
    :return:
    """
    list_1 = [((np.random.randint(0,10)),(np.random.randint(0,10))) for _ in range(10)]
    print(list_1)
    list_1.sort(key=lambda list1:list1[1],reverse=True)
    return list_1
def zad_2(pow_):
    """
    Реализуйте пример замыкания (например, «инкрементатор»)​
    :return:
    """
    def power(x):
        return x**pow_
    return power
# power_2 = zad_2(2)
# print(power_2(10))
zad_3 = lambda pow_: (lambda x: x ** pow_) # Задание 2 через лямбду
# power_2 = zad_3(3)
# print(power_2(5))

def zad_4(string):
    """
    Написать генератор, возвращающий по очереди все слова, входящие в предложение.​
    :return:
    """
    string = string.split(' ')
    count = 0
    while True:
        yield string[count]
        count += 1
# string = "Написать генератор, возвращающий по очереди все слова, входящие в предложение.​"
# slova_zad = zad_4(string)
# print(next(slova_zad))
# print(next(slova_zad))

def zad_5(seed, razr = 2):
    """
    Написать генератор псевдо случайных чисел​
        Генератор внутри задается какой-нибудь формулой, которая выдает «случайный» результат​
        На вход генератору приходит seed – начальное значение, при одинаковых начальных значениях два
        генератора будут выдавать одинаковые следующие значения​
    :return:
    """
    razr = 10**razr
    x = seed
    a = 1664525
    c = 1013904223
    m = 2**32
    count = 0
    while True:
        x = (a * x + c) % m % razr
        yield x
        count += 1
# gen = zad_5(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))

def zad_6():
    """
    Написать корутину, которая реализует бесконечную арифметическую прогрессию
    с возможностью перезапуска с любого места (3, 4, 5, 6, send(30), 31, 32, 33, …)​
    :return:
    """
    count = 0
    while True:
        count += 1
        start = yield count
        if start is not None:
            count = start
# gen_arf = zad_6()
# print(next(gen_arf))
# print(gen_arf.send(16))

def decor_zad_6(func):
    """
    Напишите декоратор, выводящий в консоль время, в которое функция была запущена.​
    :return:
    """

    def wrapper(*args):
        print(datetime.datetime.now())
        result = func(*args)
        return result
    return wrapper


def fab_decor_zad_7(max_len=10):
    def decor_zad_7(func):
        """
        Написать следующие декораторы:​
            декоратор, замеряющий время выполнения функции и выводящий информацию в консоль​

            декоратор, кэширующий результаты функции и при каждом вызове обращающийся сначала
            в кэш чтобы проверить, нет ли результата в уже посчитанных. Декоратор не должен зависеть
            от количества аргументов декорируемой функции​

        Дополнительное задание: реализовать предыдущие декораторы и, используя их,
        написать две реализации вычисления числа Фибоначчи, одну – наивную,
        вторую – с кэшированием значений с помощью декоратора.
        Сравнить время их выполнения для 30 и 80 чисел последовательности Фибоначчи​
        :return:
        """
        func.my_count = 0   # Атрибут для подсчета количества вызовов
        def wrapper(*args):

            func.__dict__['my_count'] += 1
            print(f"Функция вызывалась {func.my_count} раз")

            if len(wrapper.__dict__) >= max_len:
                list_dict = list(wrapper.__dict__.items())
                list_dict.sort(key=lambda i: i[1][1])
                wrapper.__dict__.pop(list_dict[0][0])

            if args in wrapper.__dict__:
                print('Результат взят из кэша')
                return wrapper.__dict__[args][0]
            else:
                result = func(*args)
                wrapper.__dict__[args] = (result,func.my_count-1)
                return result
        return wrapper
    return decor_zad_7


@fab_decor_zad_7(4)
def power(n):
    list_1 = [1,1]
    for i in range(n-2):
        a = list_1[1]
        list_1[1] = list_1[0]+list_1[1]
        list_1[0] = a
    return list_1[1]

for i in range(100):
    power(i)
print(power.__dict__)
