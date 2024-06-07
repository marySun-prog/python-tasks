import sys
# создаем 8 переменных типа: None, int, float, str, list, tuple, dict, set
none = None
i = int()
f = float()
string  = str()
lst = list()
tple = tuple()
dst = dict()
Set = set()
# печатаем в командную строку тип каждой переменной
print('Тип переменной none - ',type(none))
print('Тип переменной i - ',type(i))
print('Тип переменной f - ',type(f))
print('Тип переменной string - ',type(string))
print('Тип переменной list - ',type(lst))
print('Тип переменной list - ',type(tple))
print('Тип переменной list - ',type(dst))
print('Тип переменной list - ',type(Set))
# для переменной типа int изменяем тип на float и наоборот
i = float(i)
print('Тип переменной i - ',type(i))
i = int(i)
print('Тип переменной i - ',type(i))

#- для переменной типа float изменяем тип на str и наоборот
f = str(f)
print('Тип переменной f - ',type(f))
f = float(f)
print('Тип переменной f - ',type(f))

#для переменных типа str, list, tuple, dict, set печатаем размер
string = "Вася"
print(f'Размер string -  {sys.getsizeof(string)} байт')
lst = [1, 2, 3]
print(f'Размер list -  {sys.getsizeof(lst)} байт')
tple= (3, 4, 5, 6, 7)
print(f'Размер tple -  {sys.getsizeof(tple)} байт')
dst = {'a': 1, 'b': 2, 'c': 3}
print(f'Размер dst -  {sys.getsizeof(dst)} байт')
Set = {1, 2, 3,4}
print(f'Размер Set -  {sys.getsizeof(Set)} байт')

#для переменных типа str, list, tuple, dict, set печатаем их длину
print(f'Длина string -  {len(string)} символов')
print(f'Длина list -  {len(lst)} элементов')
print(f'Длина tple -  {len(tple)} элементов')
print(f'Длина dst -  {len(dst)} элементов')
print(f'Длина Set -  {len(Set)} элементов')

#для переменных типа str, list, tuple печатаем первый и последний элементы
print(f"Первый и последний элемент строки: {string[0]} и {string[-1]}")
print(f"Первый и последний элементы списка: {lst[0]} и {lst[-1]}")
print(f"Первый и последний элементы кортежа: {tple[0]} и {tple[-1]}")

#для переменных типа str, list, tuple печатаем элементы кроме первого и последнего
print(f"Элементы строки, кроме первого и последнего: {string[1:-1]}")
print(f"Элементы списка, кроме первого и последнего: {lst[1:-1]}")
print(f"Элементы кортежа, кроме первого и последнего: {tple[1:-1]}")

#для переменной типа dict печатаем значение одного из ключей 
key_to_print = 'b'  
print(f"Значение ключа '{key_to_print}': {dst[key_to_print]}")