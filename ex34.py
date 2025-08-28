try:
    salario_atual = float(input("Digite o salário atual do funcionário: R$ "))
    tempo_servico = int(input("Digite o tempo de serviço na empresa (em anos): "))
    
    reajuste = 0.0
    bonus = 0.0
    
    # Determina o percentual de reajuste
    if salario_atual <= 500.00:
        reajuste = 0.25
    elif salario_atual <= 1000.00:
        reajuste = 0.20
    elif salario_atual <= 1500.00:
        reajuste = 0.15
    elif salario_atual <= 2000.00:
        reajuste = 0.10
    
    # Determina o bônus
    if tempo_servico > 10:
        bonus = 500.00
    elif tempo_servico >= 7:
        bonus = 300.00
    elif tempo_servico >= 4:
        bonus = 200.00
    elif tempo_servico >= 1:
        bonus = 100.00
        
    if reajuste > 0 or bonus > 0:
        salario_final = salario_atual * (1 + reajuste) + bonus
        print(f"\nSalário final reajustado: R$ {salario_final:.2f}")
    else:
        print("\nO funcionário não tem direito a nenhum aumento.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos válidos.")