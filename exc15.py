def calcular_media_lista(lista):
    if len(lista) == 0:
        return None
    
    soma = sum(lista)
    media = soma / len(lista)
    return media

# Exemplo de uso:
minha_lista = [10, 20, 30, 40, 50]
media_calculada = calcular_media_lista(minha_lista)

if media_calculada is not None:
    print(f"A lista utilizada foi: {minha_lista}")
    print(f"A média dos valores da lista é: {media_calculada:.2f}")
else:
    print("A lista está vazia, não é possível calcular a média.")