#3.10:enhancedtimeconv.py
seconds = int(input('Digite o numero de segundos: '))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(hours, ':', sep='', end='')

tens = minutes//10
ones = minutes%10
print(tens, ones, ':', sep='', end='')

tens = seconds//10
ones = seconds%10
print(tens, ones, sep='')
