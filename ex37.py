try:
    valor_hora = float(input("Digite o valor que você ganha por hora: R$ "))
    horas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

    salario_bruto = valor_hora * horas_mes

    # Descontos
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    
    descontos_totais = ir + inss + sindicato
    salario_liquido = salario_bruto - descontos_totais

    # Impressão dos resultados
    print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto de Imposto de Renda (11%): R$ {ir:.2f}")
    print(f"Desconto de INSS (8%): R$ {inss:.2f}")
    print(f"Desconto do Sindicato (5%): R$ {sindicato:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")