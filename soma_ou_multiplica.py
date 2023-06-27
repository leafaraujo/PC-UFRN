contador = int(input('Qual o valor de N?'))
lista_number = []
if contador < 2:
    while contador < 2:
        print('N deve ser maior ou igual a 2!')
        contador = int(input('Digite um novo valor para N!'))
        if contador >= 2:
            print('Digite os números:')
            for i in range(contador):
                number = int(input(''))
                lista_number.insert(i, number)
else:
    print('Digite os números:')
    for i in range(contador):
        number = int(input(''))
        lista_number.insert(i, number)
operacao = int(input('Qual é a operação? Digite 0 para soma e 1 para multiplicação'))
a = int(input('Qual o A?'))
b = int(input('Qual o B?'))
if a > contador or b > contador:
    while a > contador or b > contador:
        print('Esses valores são inválidos!')
        a = int(input('Digite um novo valor para A!'))
        b = int(input('Digite um novo valor para B!'))
        ind_a = lista_number[a-1]
        ind_b = lista_number[b-1]
        if operacao == 0:
            print(f'{ind_a} + {ind_b} = {ind_a + ind_b}')
        elif operacao == 1:
            print(f'{ind_a} * {ind_b} = {ind_a * ind_b}')
else:
    ind_a = lista_number[a - 1]
    ind_b = lista_number[b - 1]
    if operacao == 0:
        print(f'{ind_a} + {ind_b} = {ind_a + ind_b}')
    elif operacao == 1:
        print(f'{ind_a} * {ind_b} = {ind_a * ind_b}')

# Crie um programa que lê um valor numérico N e que em seguida lê N números. Armazene esses números em uma lista.
# Em seguida, leia do usuário 3 números inteiros (OP, A e B). O primeiro número (OP) representa uma operação
# matemática (0 é soma, 1 é multiplicação) que deve ser realizada em cima dos dois números cujas posições (1 a N)
# na lista são A e B. O programa deve então apresentar a operação e seu resultado.
