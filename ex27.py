try:
    ano = int(input("Digite um ano para verificar se é bissexto: "))
    
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido (número inteiro).")