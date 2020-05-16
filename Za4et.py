"""
На вход подается название города, страны и список улиц.
Эти данные необходимо проверить на корректность
(что в улицу не затесались переносы строк, запятые, восклицательные знаки,
тип был str и т.д., при возникновении – исключение).
Данные также могут быть переданы в виде json строки или файла,
в котором лежит json строка. Формат и необходимые функции вы определяете сами.
"""
import random
import re
import json

FILENAME = 'za4.txt'    # Название файла с структурой данных
data = {                # Переменная с структурой данных для альтернативного ввода
 "country": ["Russia","Belarussia"],
 "city": ["SPb", "Minsk"],
 "street": ["tesr", "tesd", "tesk", "test"]
}
# with open(FILENAME, 'w') as f:
#     json.dump(data, f, indent=4)

def fab_dec_adress_gen(string_):
    """
    Декоратор принимает строку
    :param string_: текст, если будет найден в одном из значений генератора, то
                    выдаст информацию по функции, например:
                    @fab_dec_adress_gen("Minsk")
                    local_gen.send(None) = 'Russia, Minsk, Aktivistov'
    :return:        Вызов функции <function adress_gen at 0x00000000> с параметрами  (args)
                    иначе обычный возврат генератора
    """
    def dec_adress_gen(func):
        """
        :param func: Функция генератор
        """
        def wrapper(*args):
            """
            :param args: Параметры генератора
            """
            local_gen = func(*args)
            adress_pattern = re.compile(fr'\b{string_}\b')
            for result in local_gen:
                if adress_pattern.search(result):
                    yield f"Вызов функции {func} с параметрами  {args}"
                else:
                    yield result
        return wrapper
    return dec_adress_gen

@fab_dec_adress_gen("Russia")
def adress_gen(input_data):
    """
    :param input_data: Вводимая информация для генератора случайных адресов в виде
                       json строки или файла
    :return: Случайный адрес на основании input_data
    """
    while True:
        if type(input_data) is str:
            try:
                with open(input_data, 'r') as f:
                    input_data = json.load(f)
            except:
                print("Проверьте правильность ввода имени файла")
                print(input_data)
                print("Введите имя файла: ", end='')
                input_data = input()
                continue
        adress_list = []
        adress_list.append(random.choice(input_data["country"]))
        adress_list.append(random.choice(input_data["city"]))
        adress_list.append(random.choice(input_data["street"]))
        result = ', '.join(adress_list)
        input_ = yield result
        if input_ is not None:
            pass


# gen = adress_gen("za4.txt") # Пример на время тестирования
# print(next(gen))