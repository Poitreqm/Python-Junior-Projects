#
# Напишите программу, которая выводит список из всех ключей, указывающих на заданное значение,
# и если нет ни одного такого значения, он возвращает пустой список. Словарь должен быть статически описан в программном коде
# и иметь следующий вид: d={1:'a',2:'b',3:'c',4:'a',5:'d',6 :'e',7:'a',8:'b'}
#


dct = {1: "a", 2: "b", 3: "c", 4: "a", 5: "d", 6: "e", 7: "a", 8: "b"}

user_find = "m"  # что ищем

key_list = []


def find_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            key_list.append(key)
    return key_list  # возвращаем список со значениями а в случае елси значения не найдены то пустой список


print(find_value(dct, user_find))
