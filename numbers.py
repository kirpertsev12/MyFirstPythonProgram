a = int(input('Введите целое число:'))

if int(a) > 0:
    print("Число положительное:", a)
else: 
    if int(a) < 0:
        print("Число отрицательное:", a)
    elif int(a) == 0:
        print("Нулевое число:", a)
    
