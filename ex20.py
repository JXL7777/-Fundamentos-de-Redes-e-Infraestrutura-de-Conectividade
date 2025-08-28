try:
    numero_dia = int(input("Digite um número inteiro entre 1 e 7: "))
    
    if numero_dia == 1:
        print("Domingo")
    elif numero_dia == 2:
        print("Segunda-feira")
    elif numero_dia == 3:
        print("Terça-feira")
    elif numero_dia == 4:
        print("Quarta-feira")
    elif numero_dia == 5:
        print("Quinta-feira")
    elif numero_dia == 6:
        print("Sexta-feira")
    elif numero_dia == 7:
        print("Sábado")
    else:
        print("Número inválido. Por favor, digite um número entre 1 e 7.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")