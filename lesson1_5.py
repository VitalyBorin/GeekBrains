vir = float(input('Введите выручку, '))
izd = float(input('Введите издержки, '))
if vir > izd:
    print ('фирма работает с выручкой')
    
elif vir < izd:
    print ('фирма работает с убытком')
else:
    print('фирма работает в ноль')
