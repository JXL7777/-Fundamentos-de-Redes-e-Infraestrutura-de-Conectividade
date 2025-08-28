def calcular_salario(horas_trabalhadas, valor_hora):
    if horas_trabalhadas <= 40:
        salario = horas_trabalhadas * valor_hora
    else:
        salario_base = 40 * valor_hora
        horas_extras = horas_trabalhadas - 40
        valor_hora_extra = valor_hora * 1.5
        salario_extra = horas_extras * valor_hora_extra
        salario = salario_base + salario_extra
    return salario

try:
    horas = float(input("Digite o número de horas trabalhadas na semana: "))
    valor = float(input("Digite o valor da sua hora de trabalho: R$ "))
    
    salario_final = calcular_salario(horas, valor)
    print(f"\nO salário a ser pago é: R$ {salario_final:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")