# Escreva um programa que receba um número N para gerar os N primeiros termos da série de Fibonacci:
# 1, 1, 2, 3, 5, 8, 13, ...

counter = int(input('Quantos números da sequência de Fibonnaci você deseja gerar?'))
n1 = 1
n2 = 1
fibonacci = [n1, n2]
for i in range(counter-2):
    n3 = n1 + n2
    fibonacci.append(n3)
    n1 = n2
    n2 = n3
sequencia = str(fibonacci)[1:-1]
print(sequencia)
