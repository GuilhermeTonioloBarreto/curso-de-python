#Podem existir situações em que você quer especificar um tipo em uma variável. Isso pode ser feito com casting.
#Python é uma linguagem orientada a objetos, e como isso usa classes para definir tipos de dados, incluindo 
#tipos primitivos.

#Casting em python é portanto feito usando funções construtoras

#int () - constrói um número inteiro a partir de um inteiro literal, um float literal (arredondando para baixo para o 
#número inteiro anterior) ou uma string literal (fornecendo a representação da string como um número inteiro)

x = int(1)
y = int(2.8)
z = int("3") 

print(x)
print(y)
print(z)

#float() - constrói um número float a partir de um inteiro literal, float literal ou uma string literal 
#(fornecendo a representação da string como um número float ou inteiro)

x = float(1)
y = float(2.8)
z = float("3") 
w = float("4.2")

print(x)
print(y)
print(z)
print(w)

#str() - constrói uma string a partir de uma variedade de tipos de dados, incluindo strings, inteiros literais e 
#float literais

x = str("s1")
y = str(2)
z = str(3.0) 

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
