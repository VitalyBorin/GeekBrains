from sys import argv

script_name, first_param, second_param, third_param = argv

work_time = int(first_param)
value_in_h = int(first_param)
bonus = int(third_param)

print(f"Заработная плата {(work_time * value_in_h) + bonus}")