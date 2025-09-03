# Escreva um programa que receba dois números inteiros fornecidos pelo usuário e compare os valores. Ao final, o programa deve exibir na tela uma das seguintes mensagens:


#   "O primeiro valor é maior."
#   "O segundo valor é maior."
#   "Não existe valor maior, os dois são iguais."

numero = int(input("digite um numero: "))
numero2 = int(input("Digite um numero: "))

if numero > numero2:
    print(f"O primeiro valor {numero} é maior ")
elif numero2 > numero:
    print(f"O segundo valor {numero} é valor " ) 
else: 
    print(f"Os dois valores são iguais")