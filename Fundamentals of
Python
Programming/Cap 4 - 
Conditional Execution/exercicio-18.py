#exercicio-18.py
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
n5 = int(input('Digite o quinto numero: '))

maximo = n1
if n2 >= maximo:
    maximo = n2
if n3 >= maximo:
    maximo = n3
if n4 >= maximo:
    maximo = n4
if n5 >= maximo:
    maximo = n5

minimo = n1
if n2 <= minimo:
    minimo = n2
if n3 <= minimo:
    minimo = n3
if n4 <= minimo:
    minimo = n4
if n5 <= minimo:
    minimo = n5

print('\nnumero maximo =', maximo, 'numero minimo =', minimo)
