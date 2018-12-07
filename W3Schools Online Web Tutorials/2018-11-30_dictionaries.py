#Dictionary
#Um dictionary é uma coleção que é desordenada, mutável e indexável. Em Python, dictionaries são escritos com chaves, e
#eles têm chaves e valores
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)

#acessando itens
#você consegue acessar os itens de um dictionary referenciando o nome da chave dele, dentro de colchetes
x = thisdict["model"]
print(x)

#Existe também um método chamado get() que te dará o mesmo resultado
x = thisdict.get("model")
print(x)

#Mudando valores
#Você consegue mudar o valor de um item específico referindo pela chave dele
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

#Loop através de um dicionário
#Você consegue realizar um loop num dicionário usando o laço de repetição for
#Quando se faz esse loop, o valor de retorno são as chaves do dicionário, mas tem métodos para retornar os valores 
#da mesma forma
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

#Checar se a chave Existe
#Para determinar se a chave está presente em um dicionário, use a palavra chave "in"
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("Sim, 'model' é uma das keys do thisdict dictionary")

#Comprimento de um dicionário
#para determinar quantos itens (key-values pais) têm em um dicionário, use o método len()
print(len(thisdict))

#adicionando itens
#adicionar um item ao dicionário é realizado usando um novo índice de chave e atribuindo um valor a ela
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#removendo itens
#existem vários métodos para remover itens de um dicionário
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#o método popitem() remove o último item inserido (em versões anteriores a 3.7, um item aleatório era removido em vez 
# do último)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

#o método del também remove o dicionário completamente
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
#print(thisdict) #eu comentei essa função pois senão vai causar um erro no terminal

#o método clear() limpa o dicionário
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

#O construtor dict()
thisdict = dict(brand = "Ford", model = "mustang", year = 1964)
#note que as palavras chaves não são literal strings
print(thisdict)