#exercicio-19.py
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
n5 = int(input('Digite o quinto numero: '))

resultado = n1 == n2 or n1 == n3 or n1 == n4 or n1 == n5 or \
    n2 == n3 or n2 == n4 or n2 == n5 or \
    n3 == n4 or n3 == n5 or n4 == n5

print('DUPLICATES' if resultado else 'ALL UNIQUE')
