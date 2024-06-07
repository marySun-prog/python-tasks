# предлагаем ввести число
number = int(input("Введите число на интервале [-100; 100] "))
if number>100 or number<-100:
    print(f'Число {number} не входит в диапазон [-100; 100]') 
else:
    if number<-50:
        print(f'Число {number} <-50') 
    else:
        if number==-50:
         print(f'Число {number} == -50') 
        else:
           if number<0 and number>-50:
              print(f'Число {number} меньше 0, но больше -50')  
           else:
               if number>0 and number<50:
                print(f'Число {number} больше 0, но меньше 50')
               else:
                  if number==50:
                    print(f'Число {number} равно 50')  
                  else: 
                     if number>50:
                        print(f'Число {number} > 50')  
   

    

