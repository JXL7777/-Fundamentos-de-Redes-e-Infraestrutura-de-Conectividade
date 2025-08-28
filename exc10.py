def calculadora(num1, num2, simbolo):
    if simbolo == '+':
        return num1 + num2
    elif simbolo == '-':
        return num1 - num2
    elif simbolo == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    elif simbolo == '*':
        return num1 * num2
    else:
        return "Símbolo de operação inválido."

try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = input("Digite o símbolo da operação (+, -, *, /): ")
    
    resultado = calculadora(n1, n2, operacao)
    print(f"\nO resultado da operação é: {resultado}")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")