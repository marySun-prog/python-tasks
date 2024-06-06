import math
import os
# энтропия по Шеннону
def calculate_entropy(message):
    # Считаем частоту каждого символа в сообщении
    frequency = {}
    for char in message:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
 
    # Рассчитываем энтропию
    entropy = 0
    for char in frequency:
        p = frequency[char] / len(message)
        entropy -= p * math.log2(p)
    return entropy

# мощность алфавита
def alphabet_power(message):
    a =  len(set(message.lower()))
    return a    

# энтропия по Хартли
def calculate_entropyH(message):
    a =  alphabet_power(message)
    entropy = math.log2(a)
    return entropy
print("Программа расчета энтропии источника сообщений")
while True:

 # Запрос имени файла у пользователя
    file_name = input("Введите имя файла: ")
    try:
    # Открытие файла в режиме чтения
        with open(file_name, 'r', encoding='utf-8') as file:
         # Чтение содержимого файла
           message = file.read()
        flag_open = input("Вывести на экран содержимое файла? y - да, n - нет ")
        if flag_open =='y':
           # Вывод содержимого файла
           print(message)
    
        print('-------------------------------------------------------')
        # вызовы функций расчета 
        small_file_name = os.path.basename(file_name)
        print(f'Расчет для файла: {small_file_name}')
        entropy = calculate_entropy(message)
        print(f'Энтропия источника сообщений по Шеннону: {entropy}')
        entropyH = calculate_entropyH(message)
        print(f'Энтропия источника сообщений по Хартли: {entropyH}')
        a = alphabet_power(message)
        print(f'Мощность алфавита: {a}')
        # избыточность алфавита для кодирования сообщения D
        d = ((entropyH-entropy)/entropyH)*100
        print(f'Избыточность алфавита: {d}')
        print('-------------------------------------------------------')
    except FileNotFoundError:
     print("Файл не найден.")
    except Exception as e:
     print(f"Произошла ошибка: {e}")
    number = int(input("Введите число 0 для выхода или любое число для продолжения работы "))
    if number==0:
        break
print("Работа с программой завершена")    

