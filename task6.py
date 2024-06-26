# Функция: в командной строке печатает: «Привет, мир!». 
def PrintHello():
    print("Привет, мир!")

#Функция: в командной строке печатает ваше имя
def PrintFio(fio):
    print(fio)

# Аргументы: a, b, c. Значения: D. Функция: считает дискриминант квадратного 
# уравнения

def Disc(a,b,c):
    return b*b-4*a*c

# Аргументы: нет. Значения: имя, возраст. Функция: спрашивает в командной строке 
#пользователя сначала его имя, потом его возраст.  
def Name_Age():
    name = input("Введите Ваше имя ")
    age = int(input("Введите Ваш возраст"))
    return f'Ваше имя - {name} возраст {age}' 

# Аргументы: целое число. Значения: буква русского алфавита. Функция: возвращает 
#букву русского алфавита в соответствии с порядковым номером. Если аргумент 
#функции больше 33, то напечатать в командной строке «Указано не правильное 
#число!».

def Alph(p):
    if  p>=33:
        return "Указано неправильное #число!"
        
    else:
        return chr(ord("А")+p-1)

    
#Вызов определенных функций
PrintHello()
PrintFio("Вощинский А.А.")
d = Disc(2,2,4)
print(f'Дискриминант уравнения = {d}')
str = Name_Age()
print(str)
c = Alph(1)
print(c)
c = Alph(10)
print(c)
c = Alph(56)
print(c)