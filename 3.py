# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
posX = int(input ('Введите x : '))
posY = int(input ('Введите y : '))
if 0 < posX and posY > 0 :
    print ('-> 1');
elif 0 > posX and posY > 0 : 
    print ('-> 2');
elif 0 > posX and posY < 0 : 
    print ('-> 3');
elif 0 < posX and posY < 0 : 
    print ('-> 4');
else:
    print (' Внимание X ≠ 0 ! и Y ≠ 0 !');