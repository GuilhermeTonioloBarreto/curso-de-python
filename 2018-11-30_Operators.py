#Python operators
#Python divide os operadores nos seguintes grupos:
# - Operadores aritméticos
# - Operadores de Atribuição
# - Operadores de comparação
# - Operadores Lógicos
# - Operadores de Identidade
# - Operadores de Associação
# - Operadores de bit a bit

#Operadores aritméticos
#Operadores aritméticos são usados com valores numéricos para apresentar operações matemáticas comunns
print("Operadores aritméticos")
x = 7
y = 2

print(x + y) #adição
print(x - y) #subtração
print(x * y) #multiplicação
print(x / y) #divisão
print(x % y) #resto da divisão
print(x ** y) #exponencial  
print(x // y) #a função divide os dois números e pega o número inteiro abaixo

#Operadores de Atribuição
#Operadores de atribuição são usados para atribuir valores para as variáveis
print("Operadores de atribuição")
x = 5
print(x)

x = 5
x+=3 #x = x + 3
print(x)

x = 5
x-=4 #x = x - 4
print(x)

x = 5
x*=4 #x = x * 4
print(x)

x = 5
x/=4 #x = x / 4
print(x)

x = 14
x%=4 #x = x % 4
print(x)

x = 5
x**=3 #x = x ** 3
print(x)

x = 5
x&=3 #x = x & 3 (converte os dois números em binário, faz a relação AND em cada bit e o resultado converte em inteiro)
#inteiro    binário
#5          0 1 0 1
#3          0 0 1 1
#5 & 3      0 0 0 1
print(x)

x = 5
x|=3 #x = x | 3 (converte os dois números em binário, faz a relação OR em cada bit e o resultado converte em inteiro)
#inteiro    binário
#5          0 1 0 1
#3          0 0 1 1
#5 | 3      0 1 1 1
print(x)

x = 13
x^=7 #x = x ^ 3 (converte os dois números em binário, faz a relação XOR em cada bit e o resultado converte em inteiro)
#inteiro    binário
#5          1 1 0 1
#3          0 1 1 1
#5 | 3      1 0 1 0
print(x)

x = 5
x>>=1 #x = x >> 1 (converte o número x em binário, desloca ele para a direita e o resultado converte em inteiro)
#inteiro    binário
#5          0 1 0 1
#5 >>= 1    0 0 1 0
print(x)

x = 9
x<<=1 #x = x << 1 (converte o número x em binário, desloca ele para a esquerda e o resultado converte em inteiro)
#inteiro        binário
#5              1 0 0 1
#5 <<= 1      1 0 0 1 0
print(x)

#Operadores de Comparação
#Operações de comparação são usadas para comparar dois valores
print("Operadores de Comparação")
x = 5
y = 3

#se a comparação for verdadeira, será printado como True. Se a comparação for falsa, será printado como False

print(x == y) #igual
print(x != y) #não igual
print(x > y) #maior que
print(x < y) #menor que
print(x >= y) #maior ou igual que
print(x <= y) #menor ou igual que

#Operadores Lógicas
#Operações lógicos são usados para combinar afirmações condicionais
print("Operadores Lógicas")
x = 5
print(x > 3 and x < 10) #operador and
print(x > 3 or x < 4) #operador or
print(not(x > 3 and x < 10)) #operador not: inverte o resultado: retorna False se o resultado for True (e vice versa)

#Operadores de identidade
#Operadores de identidade são usados para comparar os objetos, não se eles são iguais, mas se eles são na verdade o mesmo
#objeto, com a mesma locação de memória
print("Operadores de Identidade")
x = ["maçã", "banana"]
y = ["maçã", "banana"]
z = x
print(x is z) #retorna True porque z é o mesmo objeto que x
print(x is y) #retorna False porque x não é o mesmo objeto que y, mesmo se eles têm o mesmo conteúdo
print(x == y) #para demonstrar a diferença entre "is" e "==". Essa comparação retorna True porque x é igual a y

print(x is not z) #retorna False, porque z é o mesmo objeto que x
print(x is not y) #retorna True, porque x não é o mesmo objeto que y, mesmo se eles têm o mesmo conteúdo
print(x != y) #para demonstrar a diferença ente "is not" e "<>": essa comparação retorna False, porque x é igual a y

#Operadores de Associação
#membership operators são usados para testar se uma sequência está presente em um objeto
print("operadores de associação")
x = ["maçã", "banana"]
print("banana" in x) #Retorna True, porque a sequência com o valor "banana" está dentro da lista
print("mexerica" in x) #Retorna False, porque a sequência com o valor "mexerica" não está dentro da lista
print("mexerica" not in x) #Retorna True, porque a sequência com o valor "mexerica" não está dentro da lista
