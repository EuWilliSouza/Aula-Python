import random

maquina = random.randint(0,10)

while True:
    usuario = int(input("Digite um numero: "))
    
    if  maquina == usuario:
        print("Você venceu")
        break
    elif usuario > maquina:
        print("Digite um numero menor")
    else:
        print("Digite um numero maior")