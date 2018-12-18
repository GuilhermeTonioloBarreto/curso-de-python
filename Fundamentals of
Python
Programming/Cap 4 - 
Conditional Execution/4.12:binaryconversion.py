#4.12:binaryconversion.py
valor = int(input('Digite um valor entre 0 e 1023: '))
string_binaria = ''

if (0 <= valor <= 1023):
    if valor >= 512:
        string_binaria += '1'
        valor %= 512
    else:
        string_binaria += '0'

    if valor >= 256:
        string_binaria += '1'
        valor %= 256
    else:
        string_binaria += '0'

    if valor >= 128:
        string_binaria += '1'
        valor %= 128
    else:
        string_binaria += '0'

    if valor >= 64:
        string_binaria += '1'
        valor %= 64
    else:
        string_binaria += '0'

    if valor >= 32:
        string_binaria += '1'
        valor %= 32
    else:
        string_binaria += '0'

    if valor >= 16:
        string_binaria += '1'
        valor %= 16
    else:
        string_binaria += '0'

    if valor >= 8:
        string_binaria += '1'
        valor %= 8
    else:
        string_binaria += '0'

    if valor >= 4:
        string_binaria += '1'
        valor %= 4
    else:
        string_binaria += '0'

    if valor >= 2:
        string_binaria += '1'
        valor %= 2
    else:
        string_binaria += '0'

    string_binaria += str(valor)

if string_binaria != '':
    print(string_binaria)
else:
    print('Nao consegue converter')
