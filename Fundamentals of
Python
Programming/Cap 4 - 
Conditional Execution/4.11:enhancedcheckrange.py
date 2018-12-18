#4.11:enhancedcheckrange.py
valor = int(input('Digite um inteiro entre 0 e 10: '))
if (valor >=0):
    if(valor <= 10):
        print('In range')
    else:
        print('O valor eh muito grande')
else:
    print('O valor eh muito pequeno')
print('Done')
