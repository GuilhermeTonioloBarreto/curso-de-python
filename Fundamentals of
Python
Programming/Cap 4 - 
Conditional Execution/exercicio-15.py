#exercicio-15.py
def code_fragment(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, " j =", j, " k =", k)

print('(a)', 'i = 5', 'j = 5', 'k = 7', ' e ---> ', end='')
code_fragment(3, 5, 7)

print('(b)', 'i = 3', 'j = 5', 'k = 5', ' e ---> ', end='')
code_fragment(3, 7, 5)

print('(c)', 'i = 7', 'j = 3', 'k = 7', ' e ---> ', end='')
code_fragment(5, 3, 7)

print('(d)', 'i = 5', 'j = 3', 'k = 3', ' e ---> ', end='')
code_fragment(5, 7, 3)

print('(e)', 'i = 5', 'j = 3', 'k = 5', ' e ---> ', end='')
code_fragment(7, 3, 5)

print('(f)', 'i = 7', 'j = 7', 'k = 3', ' e ---> ', end='')
code_fragment(7, 5, 3)
