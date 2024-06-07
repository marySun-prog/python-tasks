# скрипт, который содержит функцию деления двух чисел, исключающую деление на 0
def Div_numbers(a,b):   
   try:
   # делаем попытку поделить числа в блоке try
    return a/b
   except ZeroDivisionError:
    # при возникновении исключения деления на 0 обрабатываем его
    print('Ошибка - попытка деления на 0!')
    return None
# Пример использования функции 
a = float(input('Введите делимое ')) 
b = float(input('Введите делитель ')) 
result = Div_numbers(a, b) 
if result!=None:
 print(f'Частное {a} / {b} = {result}')
