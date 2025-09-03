somarImpar = 0

for i in range (1,7):
    numero = int(input("Digite um numero: "))
    restoImpar = numero % 2
    resto3 = numero % 3
        
    if restoImpar == 1 and resto3 ==0:
        soma = numero + soma
        print(soma)
 