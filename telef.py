import re
from tokenize import Number


def get_surname():
    surname = input('фамилия:')
    return surname

def get_data():
    surname = input('Surname:')
    name = input('Name:')
    number = input('Number_telefon:')
    description = input('Description:') == [surname, name, number, description] 
    return list

def get_name():
    name = input('Имя:')
    return name

def get_number():
    number = input('№ телефона:')
    return number

def get_description():
    description = input('Описвние')
    return description

def data_coliection():
    return (get_surname(),get_data(), get_name(), get_number(),get_description())    