def ordenar_numeros():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        n3 = float(input("Digite o terceiro número: "))

        numeros = [n1, n2, n3]
        numeros.sort()

        print("Os números em ordem crescente são:")
        print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")

ordenar_numeros()