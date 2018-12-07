#Diferente de outras linguagens de programação, Python não tem comando para a declaração de variáveis
#Uma variável é criada no momento em que você atribui um valor para isto
x = 5
y = "John"
print(x)
print(y)

#Variáveis não precisam ser declaradas em nenhum tipo particular e podem mesmo mudar o tipo depois de 
#terem sido configuradas

z = 4 #z é do tipo int
z = "Sally" #z é do tipo str
print(z) #o valor de z exibido foi igual ao último valor atribuído a ele, ou seja, do tipo str

#Variáveis de Saída
#Para combinar texto e uma variável, Python usa o caractere +

w = "awesome"
print("Python is " + w)

x = "Python is "
y = "awesome"
z = x + y
print(z)

#Para números, o caractere + trabalha como um operador matemático
x = 5
y = 10
print(x + y)

