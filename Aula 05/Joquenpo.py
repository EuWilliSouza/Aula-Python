import random 
lista = ["Pedra", "Papel", "Tesoura"]
maquina = random.choice(lista)


usuario = input("Descreva uma das opções do joquenpô: ")


if maquina == "Pedra" and usuario == "Papel":
    print("Usuario ganhou")
elif maquina == "Pedra" and usuario == "Tesoura":
    print("Maquina ganhou")
elif maquina == "Papel" and usuario == "Tesoura":
    print("Usuario ganhou")
elif maquina == "Papel" and usuario == "Pedra":
    print("Maquina ganhou")
elif maquina == "Tesoura" and usuario == "Pedra":
    print("Usuario ganhou")
elif maquina == "Tesoura" and usuario == "Papel":
    print("Maquina ganhou")
else:
    print("Empate")
    
print(maquina)
