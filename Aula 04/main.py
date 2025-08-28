nota = int(input("digite sua nota "))
nota2 = int(input("digite sua nota "))

media = (nota + nota2) / 2

if media >= 70:
    print("Aprovado")
    
elif media >= 50:
    print("Recuperação")
    recuperacao = int(input("Digite a nota de recuperação: "))
    mediaRecuperacao = (media + recuperacao ) / 2
    
    if mediaRecuperacao >= 70:
        print("Aprovado")
    else:
        print("Recuperação")

       
else:
    print("Reprovado")