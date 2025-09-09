#lista = []
#tupla = ()
#dicionario = {}

produto = {
    "Tipo" : "Notebook",
    "Preco" : 5000,
    "Marca" : "Positivo"
    
}
# Adicionar itens no dicionario
produto["Memoria Ram"] = "8gb ram"

#Alterar o valor do item em um dicionario 
produto["Preco"] = 6000

#Remover um item 
del produto["Memoria Ram"]

for key, value in produto.items():
    print(f"{key} - {value}")