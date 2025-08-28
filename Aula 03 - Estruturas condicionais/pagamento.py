#Simular um sistema de pagamento
#Crédito - Total
#Pix - 5% desconto

valor = int(input("Digite um numero: "))
print("Metodo de pagamentos")
print("1 - Crédito")
print("2 - PIX ")
metodoPagamento = input("Digite o metodo de pagamento: ")

if metodoPagamento == "1" :
    print(f"O valor a ser pago sera de pagamento R$ {valor:.2f}")
else:
    valorFinal = valor * 0.95
    print(f"O valor a ser pago com desconto será de R$ {valorFinal:.2f}")
    
    

