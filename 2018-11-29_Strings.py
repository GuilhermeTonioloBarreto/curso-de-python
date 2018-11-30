#String literals em python são cercados por aspas simples, ou com aspas duplas
#'hello' é o mesmo que "hello"

#Strings podem ser enviados para a tela usando a função print
print("hello")
print('olá a todos')

#Como muitas outras linguagens de programação populares, strings em Python são arrays de bytes representando caracteres
#unicodes. Entretanto, Python não tem um tipo de dado caractere, um simples caractere é uma string de comprimento 1.
#Colchetes quadrados podem ser usados para acessar elementos do string

a = "Hello, World!"
print(a[0]) #O array string começa com o índice 0
print(a[5])

#substring: Pegar os caracteres da posição 2 até a posição 5 (não incluso):
b = "Hello, world!"
print(b[2:5]) #o indice 5 não é incluso no print

#o método strip() remove todo espaço em branco do início ou do fim
a = "   Hello, world!   "
print(a)
print(a.strip()) #retorna "Hello, world!"

#o método len() retorna o comprimento de um string
a = "Hello, world!"
print(len(a))

#o método lower() retorna a string em letras minúsculas
a = "Hello, world! 123"
print(a.lower())

#o método upper() retorna a string em letras maiúsculas
a = "Hello, world! 123"
print(a.upper())

#o método replace() substitui uma string com outra string
a = "Hello, world!"
print(a.replace("H", "J"))
print(a.replace("W", "J")) #tem diferenciação entre letras maiúsculas e minúsculas
print(a) #o comando não muda a string original

#o método split() divide a string em substrings se ele encontrar instancias do separador
a = "Hello, world!"
print(a.split(","))

#Entrada de string na linha de comando
#Python permite a entrada via linha de comando
#isso significa que podemos perguntar pelo usuário por entrada
#Os exemplos a seguir pergunta pelo nome do usuário, então, usando o método input(), o programa printa o nome da pessoa
#na tela

print("Entre com seu nome: ")
x = input()
print("Olá, " + x)