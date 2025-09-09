#  Desafio para os alunos: Cadastro de Estudante Universitário com Previsão de Conclusão do Curso

# Descrição:

# Crie um programa que leia nome, idade e matrícula (número de matrícula) de um estudante universitário e os armazene em um dicionário.

# Se a matrícula for diferente de zero, o programa também deve solicitar:

# Ano de ingresso no curso

# Duração total do curso em anos

# Com essas informações, o programa deve calcular e armazenar no dicionário o ano previsto de conclusão do curso.

# Ao final, o programa deve exibir todas as informações cadastradas.

# Digite seu nome: João
# Digite sua idade: 20
# Digite seu número de matrícula: 12345
# Digite o ano de ingresso: 2022
# Digite a duração do curso em anos: 4

# --- Cadastro Completo ---
# nome - João
# idade - 20
# matricula - 12345
# ano_ingresso - 2022
# duracao_curso - 4
# ano_conclusao - 2026

Estudantes = { 
         "Nome" : input("Digite seu nome: "),
         "Idade" : int(input("Digite sua idade")),
         "Matricula" : int(input("Digite sua matricula")),         
         }

if Estudantes["Matricula"] != 0:
    Estudantes["Ano de ingresso"] = int(input("Digite o ano de ingresso: "))
    Estudantes["Duração"] = int(input("Digite o tempo de duração: "))
    
    previsao
