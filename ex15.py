try:
    valor_hora = 40.50
    imposto_renda = 0.11

    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    
    salario_bruto = horas_trabalhadas * valor_hora
    
    if salario_bruto > 2500.00:
        desconto_ir = salario_bruto * imposto_renda
        salario_liquido = salario_bruto - desconto_ir
        print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
        print(f"Desconto de Imposto de Renda (11%): R$ {desconto_ir:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    else:
        salario_liquido = salario_bruto
        print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
        print("Não há desconto de Imposto de Renda.")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para as horas trabalhadas.")