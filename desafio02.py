trabalhado = {
    "Nome" : input("Digite o seu nome "),
    "Idade" : int(input("Digite a sua idade: ")),
    "CTPS" : int(input("Digite a CTPS"))    
}

if trabalhador ["CTPS"] != 0:
    trabalhador ["Tempo de contribuição"] = int(input("Digite o tempo de contribuição: "))
    trabalhador ["Salario"] = int(input("Digite o seu salario: "))
    idadeAposentadoria = trabalhado ["idade"] + 35 - trabalhador ["Tempo de contribuição"]
    tralhador ["Idade Aposentadoria"] = idadeAposentadoria
    
    for chave, valor in trabalhador.itens():
        print(f"(chave) - (valor)")

