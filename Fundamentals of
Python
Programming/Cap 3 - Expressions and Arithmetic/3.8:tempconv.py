#Arquivo 3.8:tempconv.py
#autor:
#Ultima data de modificacao: 2018-12-11
#Converte graus Fahrenheit em graus celsius

#Solicita ao usuario a temperatura para converter e le o valor fornecido
degreesF = float(input('Enter com a temperatura em graus Fahrenheit: '))
degreesC = 5/9*(degreesF - 32)
print(degreesF, 'degrees F =', degreesC, 'degress C')
