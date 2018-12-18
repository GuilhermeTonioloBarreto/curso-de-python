#4.17:digittoword.py
value = int(input('Digite um numero entre 0 e 5:'))
if value < 0:
    print('Muito pequeno!')
else:
    if value == 0:
        print('zero')
    else:
        if value == 1:
            print('um')
        else:
            if(value == 2):
                print('dois')
            else:
                if (value == 3):
                    print('tres')
                else:
                    if value == 4:
                        print('Quatro')
                    else:
                        if value == 5:
                            print('cinco')
                        else:
                            print('muito grande')
print('Done')
