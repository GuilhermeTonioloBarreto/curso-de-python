#4.14:troubleshoot.py
print('Help! Meu PC nao funciona')
print('O computador faz algum barulho (fans, ect)')
choice = input('ou mostra alguma luz? (y/n): ')

if choice == 'n':
    choice = input(print('O computador estah plugado? (y/n): '))
    if choice == 'n':
        print('O computador estah plugado. Se o problema persistir,')
        print('Por favor, rode este programa de novo')
    else:
        choice = input('A chave estah na posicao de \'ligado\'? (y/n): ')
        if choice == 'n':
            print('Coloque no modo ligado. Se o problema persistir,')
            print('por favor, rode este programa de novo')
        else:
            choice = input('O computador tem um fusivel? (y/n): ')
            if choice == 'n':
                choice = input('Is the outlet OK? (y/n): ')
                if(choice == 'n'):
                    print('Por favor, checar o outlet circuit')
                    print('breaker or fuse. Move to a')
                    print('new outlet, if necessary. ')
                    print('If the problem persist, ')
                    print('please run this program again')
                else:
                    print('Please consult a service technical')
            else:
                print('Check the fuse. Replace if ')
                print('necessary. If the problem ')
                print('persists, then ')
                print('please run this program again')
else:
    print('Please consult a service technical')
