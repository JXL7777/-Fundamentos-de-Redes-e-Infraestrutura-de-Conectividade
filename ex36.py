try:
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    if altura > 0 and peso > 0:
        imc = peso / (altura ** 2)

        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do Peso")
        elif imc <= 24.9:
            print("Classificação: Saudável")
        elif imc <= 29.9:
            print("Classificação: Peso em excesso")
        elif imc <= 34.9:
            print("Classificação: Obesidade Grau I")
        elif imc <= 39.9:
            print("Classificação: Obesidade Grau II (severa)")
        else:
            print("Classificação: Obesidade Grau III (mórbida)")
    else:
        print("Peso e altura devem ser valores positivos.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")