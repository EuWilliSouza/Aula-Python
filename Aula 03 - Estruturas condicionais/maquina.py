import random 

maquina = random.randint(0,5)
valorUsuario = int(input("digite o numero: "))

if maquina == valorUsuario:
    print("Você acertou um numero secreto")
else:
    print("Você não acertou o numero")
    
print(maquina)

