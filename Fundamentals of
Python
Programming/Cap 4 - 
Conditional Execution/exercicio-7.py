#exercicio-7.py
x, y = 3, 5
b1, b2, b3, b4 = True, False, x == 3, y < 3

#b1 eh True
#b2 eh False
#b3 eh True
#b4 eh False

print('(a)', b3, 'eh', True)
print('(b)', b4, 'eh', False)
print('(c)', not b1, 'eh', False)
print('(d)', not b2, 'eh', True)
print('(e)', not b3, 'eh', False)
print('(f)', not b4, 'eh', True)
print('(g)', b1 and b2, 'eh', False)
print('(h)', b1 or b2, 'eh', True)
print('(i)', b1 and b3, 'eh', True)
print('(j)', b1 or b3, 'eh', True)
print('(k)', b1 and b4, 'eh', False)
print('(l)', b1 or b4, 'eh', False)
print('(m)', b2 and b3, 'eh', False)
print('(n)', b2 or b3, 'eh', True)
print('(o)', b1 and b2 or b3, 'eh', True)
print('(p)', b1 or b2 and b3, 'eh', True)
print('(q)', b1 and b2 and b3, 'eh', False)
print('(r)', b1 or b2 or b3, 'eh', True)
print('(s)', not b1 and b2 and b3, 'eh', False)
print('(t)', not b1 or b2 or b3, 'eh', True)
print('(u)', not (b1 and b2 and b3), 'eh', True)
print('(v)', not (b1 or b2 or b3), 'eh', False)
print('(w)', not b1 and not b2 and not b3, 'eh', False)
print('(x)', not b1 or not b2 or not b3, 'eh', True)
print('(y)', not (not b1 and not b2 and not b3), 'eh', True)
print('(z)', not (not b1 or not b2 or not b3), 'eh', False)
