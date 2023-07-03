number_of_players = int(input('Digite a quantidade de jogadores a ser avaliada!'))
saques = []
bloqueios = []
ataques = []
saques_certos = []
bloqueios_certos = []
ataques_certos = []

for i in range(number_of_players):
    nome_jogador = input('Qual o nome do jogador?')
    s, b, a, s1, b1, a1 = input('').split(" ")
    saques.append(int(s))
    bloqueios.append(int(b))
    ataques.append(int(a))
    saques_certos.append(int(s1))
    bloqueios_certos.append(int(b1))
    ataques_certos.append(int(a1))

print('As estatísticas do jogo são as seguintes:')
percentual_saque = (sum(saques_certos) / sum(saques)) * 100
percentual_bloqueio = (sum(bloqueios_certos) / sum(bloqueios)) * 100
percentual_ataque = (sum(ataques_certos) / sum(ataques)) * 100
print(f'Pontos de saque: {round(percentual_saque, 2)} %')
print(f'Pontos de bloqueio: {round(percentual_bloqueio, 2)} %')
print(f'Pontos de ataque: {round(percentual_ataque, 2)} %')

# O algoritmo pede a quantidade de jogadores a ser analisada, armazena seus dados de saques e bloqueios certos e total
# e dá o percentual de acertos.
