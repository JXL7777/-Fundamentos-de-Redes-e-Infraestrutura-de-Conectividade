def calculadora_menu():
    print("Escolha a opção:")
    print("1- Soma de 2 números.")
    print("2- Diferença entre 2 números (maior pelo menor).")
    print("3- Produto entre 2 números.")
    print("4- Divisão entre 2 números.")
    
    try:
        opcao = int(input("Digite o número da opção desejada: "))
        
        if opcao in [1, 2, 3, 4]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == 1:
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            elif opcao == 2:
                if num1 >= num2:
                    resultado = num1 - num2
                else:
                    resultado = num2 - num1
                print(f"A diferença entre os números é: {resultado}")
            elif opcao == 3:
                resultado = num1 * num2
                print(f"O produto entre os números é: {resultado}")
            elif opcao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"A divisão entre os números é: {resultado}")
                else:
                    print("Erro: O denominador não pode ser zero.")
        else:
            print("Opção inválida.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para a opção e valores numéricos para os cálculos.")

calculadora_menu()