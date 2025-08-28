def mini_calculadora_loop():
    while True:
        print("\n--- Menu de Opções ---")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 5:
                print("Saindo da calculadora. Até mais!")
                break
            
            if 1 <= opcao <= 4:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == 1:
                    resultado = num1 + num2
                    print(f"O resultado da adição é: {resultado}")
                elif opcao == 2:
                    resultado = num1 - num2
                    print(f"O resultado da subtração é: {resultado}")
                elif opcao == 3:
                    resultado = num1 * num2
                    print(f"O resultado da multiplicação é: {resultado}")
                elif opcao == 4:
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"O resultado da divisão é: {resultado}")
                    else:
                        print("Erro: O denominador não pode ser zero.")
            else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

mini_calculadora_loop()