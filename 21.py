# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


f = input('Введите строку:\n')

def del_some_words(f):
    f = list(filter(lambda x: 'абв' not in x, f.split()))
    return " ".join(f)

f = del_some_words(f)
print(f)