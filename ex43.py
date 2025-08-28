def calcular_media_ginastica():
    nome_atleta = input("Digite o nome do atleta: ")
    notas = []
    
    print("Digite as notas dos 7 jurados:")
    for i in range(1, 8):
        try:
            nota = float(input(f"Nota {i}: "))
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")
            return # Encerra o programa se a entrada for inválida

    if len(notas) == 7:
        melhor_nota = max(notas)
        pior_nota = min(notas)

        soma_notas = sum(notas)
        soma_restantes = soma_notas - melhor_nota - pior_nota
        media = soma_restantes / 5

        print("\nResultado final:")
        print(f"Atleta: {nome_atleta}")
        print(f"Melhor nota: {melhor_nota}")
        print(f"Pior nota: {pior_nota}")
        print(f"Média: {media:.2f}")
    else:
        print("Não foi possível processar as notas. Certifique-se de digitar 7 notas válidas.")

calcular_media_ginastica()