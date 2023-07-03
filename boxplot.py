import sys
counter_n = int(input('Qual a quantidade de valores a ser analisada?'))
first_quartil = round((1/4) * counter_n)
third_quartil = round((3/4) * counter_n)
dados = []
if counter_n <= 2:
    while counter_n <= 2:
        print('Os valores devem ser maior que 2')
        counter_n = int(input('Informe uma quantidade de valores válida!'))


print('Digite os dados:', end=' ')
dado = float(input(''))
dados.append(dado)
for i in range(counter_n - 1):
    dado = float(input(''))
    if dado < dados[i-1]:
        print('Erro! Conjunto tem de estar em ordem crescente!')
        sys.exit()
    else:
        dados.append(dado)

metade_lista = int(counter_n / 2)
if counter_n % 2 == 0:
    mediana = (dados[metade_lista] + dados[metade_lista + 1]) / 2
else:
    mediana = dados[metade_lista]

limite_inf = mediana - 3/2 * (dados[third_quartil]) - (dados[first_quartil])
limite_sup = mediana + 3/2 * (dados[third_quartil]) - (dados[first_quartil])
inferior = 0
superior = 0
counter = 0

while counter < metade_lista:
    if dados[counter] < limite_inf:
        counter += 1
    else:
        inferior = dados[counter]
        break

counter = -1
while counter > (-metade_lista):
    if dados[counter] > limite_sup:
        counter -= 1
    else:
        superior = dados[counter]
        break

print(f'Limite inferior: {int(inferior)}')
print(f'Primeiro quartil: {int(dados[first_quartil - 1])}')
print(f'A Mediana é: {int(mediana)}')
print(f'Terceiro quartil: {int(dados[third_quartil])}')
print(f'O limite superior é: {int(superior)}')

# Criação de um boxplot que informa ao usuário os limites inferior e superios, primeiro e terceiros quartis e a mediana de uma série de valores
