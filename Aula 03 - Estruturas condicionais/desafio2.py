# Desafio 02
# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

distanciaViagem = int(input("Digite a distancia percorrida em Km: "))

if distanciaViagem <= 200 :
    calculo = distanciaViagem * 0.50
    print("O valor da viagem é: ", calculo)
    
else :
    calculo2 = distanciaViagem * 0.45
    print("O valor da viagem é: ", calculo2)