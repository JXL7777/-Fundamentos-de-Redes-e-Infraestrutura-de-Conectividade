try:
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    nota3 = float(input("Digite a nota da terceira prova: "))
    
    # Pesos
    peso1 = 1
    peso2 = 1
    peso3 = 2
    
    # Cálculo da média ponderada
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    
    print(f"\nA média do aluno é: {media_ponderada:.2f}")
    
    if media_ponderada >= 60:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos para as notas.")