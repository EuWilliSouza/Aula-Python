somaPar = 0
somarImpar = 0


for i in range (1,7):
    valor = int(input("Digite um numero: "))
    resto = valor % 2
    
    if resto == 0:
        print("PAR")
        somarPar = valor + somaPar
        print(somaPar)
    else:
        print("IMPAR")
        somarImpar = valor + somarImpar
        print(somarImpar)
        