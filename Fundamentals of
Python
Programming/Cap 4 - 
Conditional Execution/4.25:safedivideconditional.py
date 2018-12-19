#4.25:safedivideconditional.py
dividendo = int(input('Entre com o dividendo: '))
divisor = int(input('Entre com o divisor: '))

print(dividendo / divisor if divisor != 0 else 'Nao pode dividir por zero')
