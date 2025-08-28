import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while True:
        try:
            chute = int(input("\nQual é o seu chute? "))
            tentativas += 1
            
            if chute < numero_secreto:
                print("O chute é menor. Tente um número maior.")
            elif chute > numero_secreto:
                print("O chute é maior. Tente um número menor.")
            else:
                print(f"\nParabéns! Você acertou o número {numero_secreto}!")
                print(f"Você precisou de {tentativas} tentativas para acertar.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

jogo_de_adivinhacao()