while True :
    try:
        
        numero = int(input("Difi=gite um numero: "))
        numero2 = int(input("Difi=gite um numero: "))

        divisao = numero / numero2
        
    except ValueError:
        print("Informe um numero")
    except ZeroDivisionError:
        print("Não é possivel dividir um numero por 0")
    