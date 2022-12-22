def get_data_from_console():
    fn = input("Введите имя: ")
    ln = input("Введите фамилию: ")
    ph = input("Введите номер телефона: ")
    co = input("Введите коментарий: ")
    bd = input("Введите дату рождения: ")
    wg_min = input('Минимальная з\п: ')
    wg_max = input("Максимальная з\п: ")
    ep = input("Должность сотрудника: ")
    return {"first_name": fn, "last_name": ln, "phone": ph, "comment": co, 'b_date': bd,
            'wg_min': wg_min, 'wg_max': wg_max, 'ep': ep}