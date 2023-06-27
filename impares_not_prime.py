n1 = int(input('Digite o valor de N1:'))
n2 = int(input('Digite o valor de N2'))
cont_divisores = 1
not_prime = []
if n1 == n2:
    print('Não existe um intervalo relevante entre dois números reais, gênio!')
elif n1 > n2:
    nulo = n1
    n1 = n2
    n2 = nulo
for count in range(n1, n2):
    for i in range(1, count):
        if count % i == 0 and count % 2 != 0:
            cont_divisores += 1
    if cont_divisores > 2:
        not_prime.append(count)
    cont_divisores = 1
numeros = str(not_prime)[1:-1]
print(f'Números ímpares não primos entre[{n1} - {n2}]:{numeros}')

# Crie um programa que leia dois números positivos n1 e n2, ambos maiores que 1, e que imprima os números ímpares
# não primos entre esses dois números, incluindo os próprios n1 e n2. Não assuma que n1 < n2. Se for ao contrário,
# troque os valores de n1 com n2.
