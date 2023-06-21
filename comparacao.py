number_1 = int(input('n1?'))
number_2 = int(input('n2?'))
number_3 = int(input('n3?'))
lista = [number_1, number_2, number_3]
lista.sort(key=int)

# Ele pede 3 números, armazena os mesmos em uma lista e depois os organiza em ordem crescente

maior = lista[-1]
menor = lista[0]
if lista.count(maior) == 1:
    print(f'Maior: {maior}')
elif lista.count(maior) > 1:
    print(f'Maiores: {maior}')
if lista.count(menor) == 1:
    print(f'Menor: {menor}')
elif lista.count(menor) > 1:
    print(f'Menores: {menor}')
if lista[1] == maior or lista[1] == menor:
    print(f'Não há intermediários nessa lista')
else:
    print(f'O número intermediário é o {lista[1]}')

# Após esse procedimento, ele verifica qual o maior, e menor elemento da lista, e se existe algum velor intermediário
