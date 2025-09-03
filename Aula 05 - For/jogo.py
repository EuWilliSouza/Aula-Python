# Ataque
# Recuperar vida 

import random

jogadorUsuario = 100
jogadorMaquina = 100

for rodada in range(1,11):
    
    print(f"===RADADA{rodada}===")
    print("INFORME A AÇÃO DESEJADA")
    print("1 - Ataque")
    print("2 - Recuperar vida")
    escolhaUser = input("Opção escolhida")
    
    if escolhaUser == "1":
        ataque = random.randint(10,15)
        jogadorMaquina = jogadorMaquina - ataque
    else:
        recuperarVida = random.randint(10,15)
        jogadorUsuario = jogadorUsuario + recuperarVida
        
        escolhaMaquina = random.randint
        
    if jogadorUsuario == 1:
        ataque = random.randint(10,15)
        jogadorUsuario = jogadorUsuario - ataque
    else:
        recuperarVida = random.randint(10,15)
        jogadorMaquina = jogadorMaquina + recuperarVida
        
    if jogadorUsuario <= 0:
        print("Você Perdeu")
        break
    
if jogadorUsuario > jogadorMaquina  and  jogadorUsuario > 0:
    print("Você perdeu")
    
elif jogadorMaquina > jogadorMaquina and jogadorMaquina > 0:
    print("Parabens, você venceu")

else:
    print("Empate")
    
    print(f"A sua vida é de {jogadorMaquina}")
    print(f"A sua vida é de {jogadorUsuario}")
    

    
        
    
        
    
    
