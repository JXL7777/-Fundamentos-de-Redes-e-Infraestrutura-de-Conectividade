def apuracao_eleicao():
    votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
    votos_nulos = 0
    votos_em_branco = 0
    
    print("Códigos de Votação:")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    print("4 - Candidato D")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("0 - Finalizar votação")
    
    while True:
        try:
            voto = int(input("\nDigite seu voto: "))
            
            if voto == 0:
                break
            elif voto in votos_candidatos:
                votos_candidatos[voto] += 1
            elif voto == 5:
                votos_nulos += 1
            elif voto == 6:
                votos_em_branco += 1
            else:
                print("Código de voto inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    total_votos = sum(votos_candidatos.values()) + votos_nulos + votos_em_branco
    
    print("\n--- Resultado da Eleição ---")
    if total_votos > 0:
        print(f"Total de votos para o Candidato A: {votos_candidatos[1]}")
        print(f"Total de votos para o Candidato B: {votos_candidatos[2]}")
        print(f"Total de votos para o Candidato C: {votos_candidatos[3]}")
        print(f"Total de votos para o Candidato D: {votos_candidatos[4]}")
        print(f"Total de votos Nulos: {votos_nulos}")
        print(f"Total de votos em Branco: {votos_em_branco}")
        
        percentual_nulos = (votos_nulos / total_votos) * 100
        percentual_brancos = (votos_em_branco / total_votos) * 100
        
        print(f"Percentual de votos nulos sobre o total: {percentual_nulos:.2f}%")
        print(f"Percentual de votos em branco sobre o total: {percentual_brancos:.2f}%")
    else:
        print("Nenhum voto foi registrado.")

apuracao_eleicao()