#🧠 Desafio 1: Calculadora de Desconto

#Descrição:
#Peça ao usuário o preço original de um produto e o percentual de desconto. Calcule o valor com desconto e mostre o resultado.

#Exemplo de entrada:
#Preço original: 100
#Desconto (%): 15

#Saída esperada:
#Preço com desconto: 85.0

precoProduto = int(input("Digite o preço do produto: "))
desconto = int(input("Digite o percentual de descontos: "))
valorDesconto = precoProduto * (desconto / 100)

precoDesconto = precoProduto - valorDesconto

print("O valor do produto com desconto é: ", )
print(f"Cada pessoa pagara R$ {precoDesconto}")



#🧠 Desafio 2: Conversor de Temperatura

#Descrição:
#Peça ao usuário uma temperatura em graus Celsius e converta para Fahrenheit.

#Fórmula: F = C × 1.8 + 32

#Exemplo de entrada:
#Temperatura em Celsius: 25

#Saída esperada:
#Temperatura em Fahrenheit: 77.0

celsius = int(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius * 1.8 + 32
print("A temperatura convertida em Fahrenheit é: ", fahrenheit)


#🧠 Desafio 3: Divisão de Conta

#Descrição:
#Peça o valor total de uma conta (como em um restaurante) e o número de pessoas. Divida o valor igualmente e mostre quanto cada pessoa deve pagar.

#Exemplo de entrada:
#Valor da conta: 120
#Número de pessoas: 4

#Saída esperada:
#Cada pessoa deve pagar: 30.0

Conta = int(input("Valor total da conta: "))
numPessoas = int(input("Numero de pessoas: "))

divisao = Conta / numPessoas

print("Cada pessoa deve pagar: ", divisao)



