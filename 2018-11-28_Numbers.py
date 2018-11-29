#Existem três tipos numéricos em Python:
#1) int
#2) float
#3) complex

#Você define o tipo de variável (int, float ou complex) a partir do número que você insere nela

x = 1 # int 
y = 2.8 # float
z = 1j # complex

print(x)
print(y)
print(z)
print(x + y + z)

#Para verificar o tipo de qualquer objeto em Python, use a função type()

print(type(x))
print(type(y))
print(type(z))

# int, ou integer, é todo número, positivo ou negativo, sem decimais, de comprimento infinito

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# float, ou "número com ponto flutuante", é um número, positivo ou negativo, contendo um ou mais decimais

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#float pode ser também um número científico com um "e" para indicar a potência de 10

x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#números complexos são escritos com um "j" como uma parte imaginária

x = 3 + 5j
y = 5j
z = -5j

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))