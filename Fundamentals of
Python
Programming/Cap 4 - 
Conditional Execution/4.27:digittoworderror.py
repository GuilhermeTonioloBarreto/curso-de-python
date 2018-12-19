#4.27:digittoworderror.py
valor = int(input('Entre com um numero entre 0 e 5: '))
resposta = 'not in range'

if valor == 0:
    resposta = 'zero'
elif valor == 1:
    resposta = 'um'
elif valor == 2:
    resposta = 'dois'
elif valor == 3:
    reposta = 'tres'
elif valor == 4:
    resposta = 'quatro'
elif valor == 5:
    resposta = 'cinco'

print('o numero que voce digitou foi', resposta)
