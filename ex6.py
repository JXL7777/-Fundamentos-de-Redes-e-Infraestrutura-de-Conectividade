def saudacao_por_turno():
    turno = input("Em que turno você estuda? Digite M (Matutino), V (Vespertino) ou N (Noturno): ").upper()
    
    if turno == 'M':
        print("Bom Dia!")
    elif turno == 'V':
        print("Boa Tarde!")
    elif turno == 'N':
        print("Boa Noite!")
    else:
        print("Valor Inválido!")

saudacao_por_turno()