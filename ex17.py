try:
    altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
    sexo = input("Digite o seu sexo (M para Masculino, F para Feminino): ").upper()
    
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    else:
        print("Sexo inválido. Por favor, digite 'M' ou 'F'.")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para a altura.")