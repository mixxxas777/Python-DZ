menu = [
    'Найти сотрудника',
    'Выборка сотруднов по должности',
    'Найти сотрудника по зп',
    'Добавить сотрудника',
    'Удалить сотрудника',
    'Обновить данные сотрудника',
    'Экспорт данных в JSON',
    'Экспорт в CSV',
    'Выход'
]


def show_menu(menu=menu):
    for i in range(len(menu)):
        print(f'[{i}] - {menu[i]}')


def show_base(data):
    count = 0
    for i in data:
        print(f'Запись номера в базу данных: {count}')
        for k in i:
            print(f'{k}: {i[k]}')
        print("*" * 20)
        count += 1