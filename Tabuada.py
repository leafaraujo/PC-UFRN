# Faça um programa que leia dois números n1 e n2, onde 1 <= n1 <= n2 <= 10, e que imprima a
# tabuada dos números entre n1 e n2, conforme exemplo.

numero_01 = int(input('Digite O primeiro número do intervalo'))
numero_02 = int(input('Agora digite o segundo número'))
if 1 > numero_01 or numero_01 > 10 or 1 > numero_02 or numero_02 > 10:
    while 1 > numero_01 or numero_01 > 10 or 1 > numero_02 or numero_02 > 10:
        print('Esses números são inválidos, N1 e N2 devem ser maiores que 1 e menores que 10!')
        numero_01 = int(input('Digite O primeiro número do intervalo'))
        numero_02 = int(input('Agora digite o segundo número'))
        if numero_02 < numero_01:
            nulo = numero_01
            numero_01 = numero_02
            numero_02 = nulo

elif numero_02 < numero_01:
    nulo = numero_01
    numero_01 = numero_02
    numero_02 = nulo

for counter in range(numero_01, numero_02 + 1):
    print(f'===== Tabuada do {counter} =====')
    for i in range(1, 11):
        print(f'{counter} x {i} = {counter*i}')
