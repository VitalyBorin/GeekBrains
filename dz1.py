from random import randint

def get_vk_friens(vk_id):
    '''Получает друзей из vk для страницы c vk_id'''
    return[{'name': 'Женя', 'bthd': '24.03.1987'},
           {'name': 'Tom', 'bthd': '24.03.1987'},
           {'name': 'ЖJohn', 'bthd': '13.03.1987'}
           ]

def get_users_with_birthday(users):
    result = []
    for user in users:
        if '24.04.' in user['bthd']:
            result.append(user)
    return result

def generate_congrat(name):
    result = ''
    words = ['Поздравляю', 'Счастья!', 'Здоровья!']
    for i in range (0, randint(1, 8)):
        result += words[randint(0, len(words)-1)]
    return f'Дорогой {name}, {result}'

def main1():
    friends = get_vk_friens('30303')
    friends_with_bthd = get_users_with_birthday(friends)
    for user in friends_with_bthd:
        print(generate_congrat(user['name']))



# friends = get_vk_friens('223423')
# print(get_users_with_birthday())
#print(generate_congrat())

main1()