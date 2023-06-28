# Crie um programa que leia um número N (0<N<10) e que imprima uma sequência de números

counter = int(input('Qual o valor de N?'))
if 1 > counter or counter > 9:
    while 1 > counter or counter > 9:
        print('O N só pode assumir valores entre 0 e 10')
        counter = int(input('Qual o valor de N?'))
for n in range(1, counter+1):
    print(f'{n}' * n)
