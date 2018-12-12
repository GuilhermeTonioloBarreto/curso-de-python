#3.9:timeconv.py
seconds = int(input('Digite o numero de segundos: '))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(hours, 'hr', minutes, 'min', seconds, 'sec')
