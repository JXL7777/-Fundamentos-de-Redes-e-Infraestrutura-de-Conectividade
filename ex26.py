try:
    idade = int(input("Digite a idade do trabalhador: "))
    tempo_servico = int(input("Digite o tempo de serviço (em anos): "))
    
    pode_aposentar = False

    if idade >= 65:
        pode_aposentar = True
    elif tempo_servico >= 30:
        pode_aposentar = True
    elif idade >= 60 and tempo_servico >= 25:
        pode_aposentar = True
        
    if pode_aposentar:
        print("O trabalhador pode se aposentar.")
    else:
        print("O trabalhador ainda não pode se aposentar.")

except ValueError:
    print("Entrada inválida. Por favor, digite números inteiros para a idade e o tempo de serviço.")