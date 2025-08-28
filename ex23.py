def mini_calculadora():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    try:
        operacao = int(input("Digite o número da operação desejada: "))
        
        if operacao not in [1, 2, 3, 4]:
            print("Opção inválida.")
            return

        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if operacao == 1:
            resultado = num1 + num2
            print(f"O resultado da soma é: {resultado}")
        elif operacao == 2:
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif operacao == 3:
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif operacao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros para a operação e números para os valores.")

mini_calculadora()