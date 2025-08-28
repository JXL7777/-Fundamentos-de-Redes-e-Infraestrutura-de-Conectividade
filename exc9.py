def calcular_media(nota1, nota2, nota3, tipo_media):
    if tipo_media.upper() == 'A':
        media = (nota1 + nota2 + nota3) / 3
        return media
    elif tipo_media.upper() == 'P':
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
        return media
    else:
        return None

try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    tipo = input("Digite o tipo de média ('A' para Aritmética ou 'P' para Ponderada): ")
    
    media_calculada = calcular_media(n1, n2, n3, tipo)

    if media_calculada is not None:
        print(f"\nA média é: {media_calculada:.2f}")
    else:
        print("Tipo de média inválido.")
        
except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos para as notas.")