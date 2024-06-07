# создаем список из 7 элементов типов None, int, float, str, list, tuple, dict
my_list = [None, 14, 3.14, "Привет, мир!", [1, 2, 3], (4, 5, 6), {"name": "Александр", "age": 22}] 
# в цикле по элементам печатаем в командной строке тип каждого элемента
for elem in my_list: 
    print(type(elem)) 
#удаляем последний элемент 
my_list.pop() 
#по строковой переменной, содержащей ваше ФИО, создаем список из букв вашего ФИО 
full_name = "Вощинский Александр" 
letters = list(full_name) 
# печатаем список букв ФИО
for elem in letters: 
    print(elem) 
#по списку из букв вашего ФИО создаем строковую переменную, содержащую ваше ФИО
full_name_back = ''.join(letters) 
print(full_name_back)   
# печатаем порядковый номер и соответствующий символ в ФИО 
for i, letter in enumerate(full_name): 
    print(i+1, letter) 

# печатаем количество символов "а" в ФИО с учетом регистра
a_count = letters.count('а') 
print("Количество символов 'а' в ФИО:", a_count)