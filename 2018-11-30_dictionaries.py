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