#3.11:faultytempconv.py
degreesF, degreesC = 0, 0
degreesC = 5/9*(degreesF - 32)
degreesF = float(input('Entre a temperatura em F: '))
print(degreesF, 'degrees F =', round(degreesC, 4), 'degrees C')
