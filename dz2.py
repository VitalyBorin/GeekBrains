time_sec_in=int(input('Введите время в секундах: '))
time_h=time_sec_in // 3600
time_m=time_sec_in % 3600 // 60
time_s=time_sec_in % 3600 % 60

#print('Время в формате Ч:М:С - ', time_h, ':', time_m, ':', time_s, sep='')
#print(f"{time_h}:{time_m}:{time_s}")
print('Время в формате ЧЧ:ММ:СС - ', f"{time_h}:{'{:02}'.format(time_m)}:{'{:02}'.format(time_s)}")
