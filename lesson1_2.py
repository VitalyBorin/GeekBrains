sec = int(input ('please enter time in seconds'))
hours = sec // 3600
print (hours)
sec = sec - hours * 3600
print (sec)
minute = sec // 60
print (minute)
sec = sec - minute * 60
print (sec)
print(f'{hours}:{minute}:{sec}')