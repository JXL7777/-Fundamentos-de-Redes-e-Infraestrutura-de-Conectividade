try:
    nota1 = float(input("Digite a primeira nota (0.0 a 10.0): "))
    
    if nota1 < 0.0 or nota1 > 10.0:
        print("Nota inválida. O programa será encerrado.")
    else:
        nota2 = float(input("Digite a segunda nota (0.0 a 10.0): "))
        if nota2 < 0.0 or nota2 > 10.0:
            print("Nota inválida. O programa será encerrado.")
        else:
            media = (nota1 + nota2) / 2
            print(f"A média das notas é: {media:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")