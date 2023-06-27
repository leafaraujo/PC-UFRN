# Escreva um programa que peça ao usuário dois números inteiros n1 e n2 (n2 > n1) e imprima quantos números primos
# existem no nintervalo [n1, n2], incluindo esses dois números. Lembre-se que um número é primo se ele é
# divisivel apenas por 1 e por ele mesmo.

n1 = int(input('N1?'))
n2 = int(input('N2?'))
prime = []
divisores = 0
if n1 > n2:
    nulo = n1
    n1 = n2
    n2 = nulo
for count in range(n1, n2):
    for i in range(1, count+1):
        if count % i == 0:
            divisores += 1
    if divisores == 2:
        prime.append(count)
    divisores = 0
print(f'Existem {len(prime)} números primos entre {n1} e {n2}')
