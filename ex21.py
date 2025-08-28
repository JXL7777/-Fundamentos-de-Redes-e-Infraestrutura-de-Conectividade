try:
    numero_mes = int(input("Digite um número inteiro entre 1 e 12: "))
    
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    if numero_mes in meses:
        print(meses[numero_mes])
    else:
        print("Número inválido. Por favor, digite um número entre 1 e 12.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")