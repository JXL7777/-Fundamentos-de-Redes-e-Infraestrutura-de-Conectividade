def analisar_dados_academia():
    maior_idade = 0
    maior_altura = 0.0
    maior_peso = 0.0
    soma_altura = 0.0
    soma_imc = 0.0
    total_homens = 0
    total_mulheres = 0

    numero_de_pessoas = 25
    
    for i in range(1, numero_de_pessoas + 1):
        print(f"\n--- Coletando dados da Pessoa {i} ---")
        try:
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ").upper()
            altura = float(input("Altura (m): "))
            peso = float(input("Peso (kg): "))

            # Atualiza a idade, altura e peso máximos
            if idade > maior_idade:
                maior_idade = idade
            if altura > maior_altura:
                maior_altura = altura
            if peso > maior_peso:
                maior_peso = peso

            # Soma para calcular a média de altura
            soma_altura += altura

            # Calcula o IMC e soma
            imc = peso / (altura ** 2)
            soma_imc += imc

            # Conta o sexo
            if sexo == 'M':
                total_homens += 1
            elif sexo == 'F':
                total_mulheres += 1
            
        except ValueError:
            print("Entrada inválida. Por favor, digite números para idade, altura e peso, e 'M' ou 'F' para o sexo.")
            # Se a entrada for inválida, pulamos para a próxima iteração
            continue

    total_pessoas_validas = total_homens + total_mulheres
    
    print("\n--- Resultados Finais ---")
    if total_pessoas_validas > 0:
        media_altura = soma_altura / total_pessoas_validas
        media_imc = soma_imc / total_pessoas_validas
        
        percentual_masculino = (total_homens / total_pessoas_validas) * 100
        percentual_feminino = (total_mulheres / total_pessoas_validas) * 100

        print(f"Idade da pessoa mais velha: {maior_idade} anos")
        print(f"Altura do mais alto: {maior_altura:.2f} m")
        print(f"Maior peso: {maior_peso:.2f} kg")
        print(f"Média de altura: {media_altura:.2f} m")
        print(f"Média de IMC: {media_imc:.2f}")
        print(f"Percentual de sexo masculino: {percentual_masculino:.2f}%")
        print(f"Percentual de sexo feminino: {percentual_feminino:.2f}%")
    else:
        print("Nenhum dado válido foi inserido para análise.")

analisar_dados_academia()