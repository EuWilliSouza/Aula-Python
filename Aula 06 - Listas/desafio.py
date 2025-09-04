listaFilmes = ["Vingadores: Ultimato", "Toy Story", "O Rei Leão", "Matrix"]

listaPreco = [25, 20, 22, 18]

for preco, filme in zip(listaPreco, listaFilmes):
    print(f"{i} - {filme} - R$ {preco}")
    i = i + 1
    
    filmeEscolhido = int(input("Digite a posição do Filme escohido: "))   
    
    print(f"Filme escolhido {listaFilmes[filmeEscolhido]} -  R$ {listaPreco[filmeEscolhido]}")


