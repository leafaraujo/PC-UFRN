dias = int(input('Qual a quantidade de dias que deseja converter em semanas?'))
if dias < 7:
    if dias == 0:
        print(f'{dias} equivale à nenhum dia!')
    elif dias == 1:
        print(f'{dias} equivale à {dias} dia!')
    else:
        print(f'{dias} equivale à {dias} dias!')
else:
    semanas = dias // 7
    dias_restantes = dias % 7
    if semanas == 1:
        if dias_restantes == 0:
            print(f'{dias} dias equivalem à {semanas} semana!')
        elif dias_restantes == 1:
            print(f'{dias} dias equivalem à {semanas} semana e {dias_restantes} dia!')
        else:
            print(f'{dias} dias equivalem à {semanas} semana e {dias_restantes} dias!')
    else:
        if dias_restantes == 0:
            print(f'{dias} dias equivalem à {semanas} semanas!')
        elif dias_restantes == 1:
            print(f'{dias} dias equivalem à {semanas} semanas e {dias_restantes} dia!')
        else:
            print(f'{dias} dias equivalem à {semanas} semanas e {dias_restantes} dias!')

# O programa acima, pede ao usuário uma quantidade de dias, e retorna o seu valor em semanas e dias restantes.
