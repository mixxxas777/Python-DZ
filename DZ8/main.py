from view_mod import show_menu as sm
from controller import *


def main():
    flag = '*'
    while flag == '*':
        sm()
        flag = controller(input("Выберите цыфру из меню: "))


if __name__ == '__main__':
    main()