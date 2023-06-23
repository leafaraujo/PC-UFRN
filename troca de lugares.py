print('Olá, sou a tIA, a inteligência artificial que vai lhe ajudar a desenhar o layout da sala de aula')
qtd_alunos = int(input('Qual a quantidade alunos da sua fileira?'))
print('Digite o nome dos alunos')
layout_fileira = []
for i in range(qtd_alunos):
    aluno = input('')
    layout_fileira.insert(i, aluno)
resto = len(layout_fileira) % 2
if resto == 0:
    metade_alunos = len(layout_fileira) // 2
    trocas = int(metade_alunos // 2)
    contador_pos = 1
    contador_neg = -1
    nulo = 0
    for i in range(trocas):
        nulo = layout_fileira[contador_pos]
        layout_fileira[contador_pos] = layout_fileira[contador_neg]
        layout_fileira[contador_neg] = nulo
        contador_pos = contador_pos + 2
        contador_neg = contador_neg - 2
else:
    metade_alunos = len(layout_fileira)
    trocas = int(metade_alunos // 2)
    contador_pos = 1
    contador_neg = -2
    nulo = 0
    for i in range(trocas):
        nulo = layout_fileira[contador_pos]
        layout_fileira[contador_pos] = layout_fileira[contador_neg]
        layout_fileira[contador_neg] = nulo
        contador_pos = contador_pos + 2
        contador_neg = contador_neg - 2
print(*layout_fileira, sep="\n")

# Em uma turma de alunos que conversavam muito, um professor montou a seguinte estratégia. Após os alunos se
# sentarem, ele mandava os alunos trocarem de lugar. Para ajudar esse processo, crie um programa para ajudar esse
# professor. O programa deve ler um valor N, que representa a quantidade de alunos. Em seguida, deve ler os nomes de
# cada aluno. Considere a sequência lida como a ordem das cadeiras dos alunos. O programa deve então imprimir os
# nomes em uma nova ordem, trocando os alunos sentados em cadeiras de número par (o da primeira cadeira par vai para
# a última par, o da segunda para a antepenúltima, etc.).

# Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, vão haver 3 cadeiras pares), o aluno da
# cadeira central não terá seu local trocado.
