#Listas
#Coleção em Python (array)
#Existem quatro tipos de dados de colecionar na linguagem de programação Python:
#1) List é a coleção que é ordenada e mutável. Permite membros duplicados
#2) Turple é uma coleção em que é ordenada e imutável. Permite membros duplicados
#3) Set é uma coleção que é desordenada e não indexada. Não permite membros duplicados
#4) Dictionary é uma coleção que é desordenada, mutável e indexada. Não permite membros duplicados

#quando se escolhe um tipo de coleção, é importante entender as propriedades de cada tipo. Escolhendo o tipo certo para
#uma configuração de dados particular pode significar conservação do propósito, e, isso pode significar um aumento na
#eficiência ou segurança

#List
#Uma List é uma coleção que é ordenada e mutável. Em Python, lists são escritas com colchetes
thislist = ["apple", "banana", "cherry"]
print(thislist) 

#Acesso a itens
#Você acessa aos itens via referindo-os pelo índice
print(thislist[0]) #como em strings, os índices começam em 0

#Mudar o valor do item
#Para mudar um valor ou um item específico, referencie o índice
thislist[1] = "blackcurrant"
print(thislist)

#Loop através da lista
#Você pode realizar um loop através da lista usando o for loop (iremos aprender mais sobre for loops no
# Python For Loops Chapter)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Checar se um item existe
#Para determinar se um item específico está presente na lista, use a palavra chave in
if "apple" in thislist:
    print("SIM, 'apple' está na lista de frutas")

#Comprimento de lista
#para determinar quantos itens uma lista tem, use o método len()
print(len(thislist))

#Adicionar itens
#Para adicionar itens para o fim da lista, use o método append() (significa acrescentar)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Para adicionar um item em um índice específico, use o método insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #inserir 'orange' no segundo índice
print(thislist)

#Remover Itens
#Existem vários métodos para remover itens da lista
#o método remove() remove um item específico
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #se escrever um nome que não contém na lista, dá erro no programa
print(thislist)

#o método pop() remove um índice específico, (ou, o último item se o índice não for especificado)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#a palavra chave del remove um índice específico
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#a palavra chave del pode remover a lista por completo
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #o certo seria printar esse resultado, mas isso iria travar o programa em si com um erro, dizendo que
#'thislist' não está mais definido (não existe mais)

#O método clear() apaga a lista
#a palavra chave del remove um índice específico
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print(len(thislist)) #ela permanece como uma lista com nenhum elemento

#O construtor list()
#Também é possível usar o construtor list() para fazer uma lista
thislist = list(("apple", "banana", "cherry"))
print(thislist)