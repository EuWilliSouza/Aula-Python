listaNomes = ["Willian, Thaís, Célia, Wilken"]

print(listaNomes)

#Listando os itens da lista

print(listaNomes[0])
print(listaNomes[1])
print(listaNomes[2])
print(listaNomes[3])

#Adicionar itens

listaNomes.append("Willian")
listaNomes.append("Thaís")
print(listaNomes)

#Adicionar itens em uma posição desejada da lista
listaNomes.insert(2, "Célia")
listaNomes.insert(3, "Willian")
print(listaNomes)

#Alterar um item da lista 
listaNomes[0] = "Willian"


#Verificar o tamanho da lista
print(len(listaNomes))

#Ordenar a lista
print(sorted(listaNomes))

#Excluir um item 
listaNomes.pop()

print(listaNomes)


for nome in listaNomes:
    print(nome)
    

