def verifica_sexo():
    letra = input("Digite uma letra (F ou M): ").upper()
    
    if letra == 'F':
        print("F - Feminino")
    elif letra == 'M':
        print("M - Masculino")
    else:
        print("Sexo Inválido")

verifica_sexo()