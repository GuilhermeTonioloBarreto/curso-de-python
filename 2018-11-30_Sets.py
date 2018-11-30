#Python Sets
#Set é uma coleção que é desordenada e desindexada. Em python, sets são escritos com chaves
thisset = {"apple", "banana", "cherry"}
print(thisset) #Set são desordenados, então os itens irão aparecer em uma ordem aleatória

#Acessar itens
#Você não consegue acessar itens em um set referenciando um índice, porque set são desordenados e os itens não têm indice
#Mas você consegue percorrer através dos itens do set usando um for loop, ou perguntar se um item específico está no set,
#usando a palavra chave in
thisset = {"banana", "apple", "cherry"}
for x in thisset:
    print(x)

#checar se "banana" está presente no set
print("banana" in thisset)

#adicionar itens
#Uma vez que um set é criado, você não consegue mudar os itens dele, mas vocẽ consegue adicionar novos itens
#para adicionar um item em um set, use o método add()
#para adicionar mais de um item em um set, use o método update()
thisset = {"banana", "cherry", "apple"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#Pegar o comprimento de um Set
#Para determiar quantos itens um set tem, use o método len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Remover itens
#Para remover um item em um set, use o método remove(), ou o método discard()
thisset.remove("banana") #Se o item a ser removido não existir, remove() vai criar um erro
print(thisset)

thisset.discard("apple") #se um item a ser removido não existir, discard() não criará um erro
print(thisset)

#Você consegue também usar o método pop() para remover um item, mas esse método irá remover o último item. Relembre que 
#sets são desordenados, então você não irá saber qual item que foi removido
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#o método clear() esvazia o set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#a palavra chave del deletará o set completamente
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #essa linha do código está comentada porque aparece um erro dizendo que o nome thisset não é definido

#O construtor set
#também é possível usar um construtor set() para fazer um set
thisset = set(("apple", "banana", "cherry")) #repare nos dois parênteses
print(thisset)