# в цикле for печатаем в командную строку числа от 0 до 10
for i in range(11):
    print(i)
    i = 0
# в цикле while печатаем в командную строку числа от 0 до 10
print('-----------------------------------------------')
while i <= 10:
    print(i)
    i += 1
# создаем строковую переменную, которая содержит ваше ФИО  
fio = "Вощинский А.А."
# в цикле for печатаем в командную строку каждую букву вашего ФИО  
print('-----------------------------------------------')
for letter in fio:
    print(letter)
# создаем список, который содержит имена ваших друзей
lst = ["Иван", "Денис", "Петр"]
# в цикле for печатаем в командную строку имена ваших друзей
print('-----------------------------------------------')
for str in lst:
    print(str)
# создает словарь, где ключами являются имена ваших друзей, а значениями их дата 
# рождения в формате день.месяц.год    
friends = {
    "Иван": "01.01.1990",
    "Денис": "02.06.1991",
    "Петр": "03.03.1992",
    "Катерина": "14.07.1992"
}
#в цикле for печатает в командную строку имена только тех друзей, которые родились 
#летом или зимой и даты их рождения;
print('-----------------------------------------------')
for name, bdata in friends.items():
     m = int(bdata.split('.')[1])
     if m in [6, 7, 8, 12, 1, 2]:
        print(f"Имя: {name}, Дата рождения: {bdata}")