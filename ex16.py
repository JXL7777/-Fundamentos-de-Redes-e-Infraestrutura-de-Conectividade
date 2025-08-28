try:
    salario = float(input("Digite o salário do trabalhador: R$ "))
    prestacao = float(input("Digite o valor da prestação do empréstimo: R$ "))
    
    limite_prestacao = salario * 0.20
    
    if prestacao > limite_prestacao:
        print("Empréstimo não concedido.")
    else:
        print("Empréstimo concedido.")

except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")