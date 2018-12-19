#exercicio-17.py

def funcao1(n):
    if n < 1000:
        print('*', end='')
    if n < 100:
        print('*', end='')
    if n < 10:
        print('*', end='')
    if n < 1:
        print('*', end='')
    print()

def funcao2(n):
    if n < 1000:
        print('*', end='')
    elif n < 100:
        print('*', end='')
    elif n < 10:
        print('*', end='')
    elif n < 1:
        print('*', end='')
    print()

print('(a)')
print('funcao 1:', '****', '= ', end='')
funcao1(0)
print('funcao 2:', '*', '= ', end='')
funcao2(0)

print('(b)')
print('funcao 1:', '***', '= ', end='')
funcao1(1)
print('funcao 2:', '*', '= ', end='')
funcao2(1)

print('(c)')
print('funcao 1:', '***', '= ', end='')
funcao1(5)
print('funcao 2:', '*', '= ', end='')
funcao2(5)

print('(d)')
print('funcao 1:', '**', '= ', end='')
funcao1(50)
print('funcao 2:', '*', '= ', end='')
funcao2(50)

print('(e)')
print('funcao 1:', '*', '= ', end='')
funcao1(500)
print('funcao 2:', '*', '= ', end='')
funcao2(500)

print('(f)')
print('funcao 1:', '', '= ', end='')
funcao1(5000)
print('funcao 2:', '', '= ', end='')
funcao2(5000)

print('\nIsso ocorre pois, na funcao1(), todas as condicoes if foram testadas.\n' +
      'ja na funcao2(), quando uma das condicoes foram verdadeiras, as outras ' +
      'nao eram testadas')
