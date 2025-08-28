def celsius_para_fahrenheit(c):
    fahrenheit = c * (9.0/5.0) + 32.0
    return fahrenheit

try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    
    fahrenheit_convertido = celsius_para_fahrenheit(celsius)
    print(f"\nA temperatura em Fahrenheit é: {fahrenheit_convertido:.2f}°F")
    
except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico.")