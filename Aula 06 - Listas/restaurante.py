listaLanches = ["X-Bacon", "X-Tudo", "Hot-Dog", "X-Salada", "X-Frango", "Batata frita com chedar", "X-Egg"]
listaPreco = [20, 30, 20, 20, 23, 20, 15, 18]


i = 1
for preco, lanche in zip(listaPreco, listaLanches):
    print(f"{i} - {lanche} - R$ {preco}")
    i = i + 1
    
    lancheEscolhido = int(input("Digite a posição do lanche escohido: "))   
    
    print(f"Lanche escolhido {listaLanches[lancheEscolhido]} -  R$ {listaPreco[lancheEscolhido]}")
    
    