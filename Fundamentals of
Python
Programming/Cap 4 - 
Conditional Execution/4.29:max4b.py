#4.29:max4b.py
print('Por favor, ente com quatro valores inteiros:')
numero1 = int(input('Entre com o numero 1: '))
numero2 = int(input('Entre com o numero 2: '))
numero3 = int(input('Entre com o numero 3: '))
numero4 = int(input('Entre com o numero 4: '))

max = numero1

if numero2 > max:
    max = numero2
if numero3 > max:
    max = numero3
if numero4 > max:
    max = numero4

print('O maximo numero digitado foi {0}'.format(max))
