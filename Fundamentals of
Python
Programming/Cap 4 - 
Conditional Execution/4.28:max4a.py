#4.28:max4a.py
print('Por favor, ente com quatro valores inteiros:')
numero1 = int(input('Entre com o numero 1: '))
numero2 = int(input('Entre com o numero 2: '))
numero3 = int(input('Entre com o numero 3: '))
numero4 = int(input('Entre com o numero 4: '))

if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4:
    max=numero1
elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4:
    max = numero2
elif numero3 >= numero1 and numero3 >= numero2 and numero3 >= numero4:
    max = numero3
else:
    max = numero4

print('O maximo numero digitado foi {0}'.format(max))
