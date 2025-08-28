# Desafio 01
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidadeCarro = int(input("Digite a velocidade: "))
velocidadeMaxima = 80
multa = velocidadeCarro - velocidadeMaxima

if velocidadeCarro > velocidadeMaxima :
    print("Você foi multado por ultrapassar o limite de velocidade: ", multa*7) 
    
else : 
    velocidadeCarro <= velocidadeMaxima 
    print("Você esta dentro da velocidade exigida, siga em frente")


    