def mf (fn, ln, yb, c, e, p):
    res = [fn, ln, yb, c, e, p]
    return res

first_name = input('Введите имя ')
last_name = input('Введите фамилию ')
year_of_birth = input('Введите год рождения ')
city = input('Введите город ')
email = input('Введите email ')
phone = input('Введите номер телефона ')

print(' '.join(mf (fn = first_name, ln = last_name, yb = year_of_birth, c = city, e = email, p = phone)))


# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.