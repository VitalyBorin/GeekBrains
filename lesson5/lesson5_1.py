str_to_file = ""
big_str = ""
print("Вводите текст. Каждую строку завершайте Enter. Если нажать Enter без ввода символов - все предыдущие строки запишутся в файл")

while True:
    str_to_file = input('')
    if not str_to_file:
        break
    big_str = big_str + str_to_file + "\n"

with open("text.txt", "w") as f_obj:
    print(big_str, file=f_obj)