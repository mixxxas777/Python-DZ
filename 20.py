# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x**2 + 5*x**3')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('3*x**2 + 9*x**3')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()
s1 = ''.join(list_of_poly_1)
with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()
s2 = ''.join(list_of_poly_2)
s = s1.split('+')+s2.split('+')
i = ' '.join(s)
int_b = i.replace(' ','+')
print(int_b)
i = re.split("'*", int_b)
print (i)
sum_poly = list_of_poly_1 + list_of_poly_2
with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{int_b}')