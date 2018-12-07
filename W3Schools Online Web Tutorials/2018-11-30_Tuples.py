#Tuples
#Uma tuple é uma coleção que é ordenada e imutável. Em Python, tuples são escritas com parênteses (round brackets)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Acessar itens da Tuple
#Você pode acessar itens da tuple referenciando o índice, dentro de colchetes
print(thistuple[1])

#Mudar valores de uma tuple
#Uma vez que uma tuple é criada, você não consegue mudar seus valores. Tuples são imutávels
thistuple = ("apple", "banana", "cherry")
#thistuple[1] = "blackcurrant" #se eu não deixar comentado, vai aparecer uma mensagem de erro, dizendo que 
#tuples não suportam atribuições de itens
print(thistuple)

#Loop através de Tuples
#Você pode realizar um loop através do tuples usando o laço de repetição for
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#Checar se o item existe
#Para determinar se um item específico está presente em um tuple, use a palavrachave in
if "apple" in thistuple:
    print("yes, " + thistuple[0] + " está dentro do fruits tuple")

#Comprimento do tuple
#Para determinar quantos itens um tuple tem, use o método len()
print(len(thistuple))

#Adicionar itens
#Uma vez que um tuple é criado, você não pode adicionar itens a ele. Tuples são imutáveis
thistuple = ("apple", "banana", "cherry")
#thistuple[3] = "orange" #está comentado pois irá gerar um erro dizendo que objetos do tipo "tuple" não suporta 
                         #atribuição de item
print(thistuple)

#Remove itens
#Tuples são imutáveis, então você não pode remover itens dele, contudo, você pode deletar o tuple completamente
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #está comentado pois aparece um erro dizendo que o nome "thistuple" não está definido

#O construtor tuple()
#É também possível usar o construtor tuple() para criar um tuple
thistuple = tuple(("apple", "banana", "cherry")) #repare nos dois parênteses
print(thistuple)
