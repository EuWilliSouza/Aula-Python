listaNotas = []

while True:
    nota = int(input("Digite sua nota ou 999 para sair: "))
    
    if nota == 999:
        break
    elif nota > 10 or nota < 0:
        print("Digite uma nota de 0 a 10")
        break
      
         
   
    listaNotas.append(nota)
    print(listaNotas)
    
    
    