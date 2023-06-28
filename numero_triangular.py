# Um número inteiro positivo,n, é dito triangular se, e somente se, ele é o resultado do produto de três números
# inteiros positivos e consecutivos. Escreva um algoritmo que leia um número inteiro positivo, n, e escreva como saída
# “é triangular” se n for triangular e “não é triangular”, caso contrário.

n = int(input('Digite o número que deseja verificar se é triangular'))
i = 1
while i * (i+1) * (i+2) < n:
    i = i + 1
if i * (i+1) * (i+2) == n:
    print(f'{n} é um número triangular!')
else:
    print(f'{n} Não é um número triangular!')
