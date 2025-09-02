#Simular um sistema de pagamento
#Crédito - Total
#Pix - 5% desconto

valor = int(input("Digite um numero: "))
print("Metodo de pagamentos")
print("1 - Crédito")
print("2 - PIX ")
print("3 - Debito ")
metodoPagamento = int(input("Digite o metodo de pagamento: "))

if metodoPagamento == 1 :
    print(f"O valor a ser pago sera de pagamento R$ {valor:.2f}")
    print("1 - Á vista")
    print("2 - 2x - 5% de juros")
    print("3 - 3x - 10% de juros")
    
    metodoParcelamento = input ("Metodo e parcelamento: ")
    
    if metodoParcelamento == "1" :
        print(f"O valor a ser pago será de R$ {valor:.2f}")
    elif metodoParcelamento =="2":
        valorFinal = valor * 1.05
        print(f"O valor a ser pago será de R$ {valorFinal:.2f}")
    elif metodoParcelamento == "3":
        valorFinal1 = valor * 1.10
        print(f"O valor a ser pago será de R$ {valorFinal1:.2f}")
        
        

    
elif metodoPagamento == 2 :
    valorPix = valor * 0.95
    print(f"O valor a ser pago com desconto será de R$ {valorPix:.2f}")
else:
    valorDebito = valor * 0.98
    print(f"O valor a ser pago com desconto será de R$ {valorDebito:.2f} ")
    
    

