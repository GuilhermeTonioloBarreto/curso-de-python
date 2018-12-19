#exercicio-16.py

def program(val):
    if val < 10:
        if val != 5:
            print("wow ", end='')
        else:
            val += 1
    else:
        if val == 17:
            val += 10
        else:
            print("whoa ", end='')
    print(val)

print('(a)', 'wow 3', '= ', end='')
program(3)

print('(b)', 'whoa 21', '= ', end='')
program(21)

print('(c)', '6', '= ', end='')
program(5)

print('(d)', '27', '= ', end='')
program(17)

print('(e)', 'wow -5', '= ', end='')
program(-5)
