import random

def sorteia_aluno(quantidade_alunos):
    lista_alunos = []
    
    print("Digite o nome dos alunos:")
    for i in range(quantidade_alunos):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        lista_alunos.append(nome)
        
    aluno_sorteado = random.choice(lista_alunos)
    return aluno_sorteado

try:
    num_alunos = int(input("Digite a quantidade de alunos para o sorteio: "))
    
    if num_alunos > 0:
        primeiro_a_apresentar = sorteia_aluno(num_alunos)
        print(f"\nO primeiro aluno(a) a apresentar será: {primeiro_a_apresentar}")
    else:
        print("A quantidade de alunos deve ser um número positivo.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")