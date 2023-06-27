qnt_nomes = int(input('Qual a quantidade de nomes?'))
print('Digite o nome dos alunos')
alunos = []
for i in range(qnt_nomes):
    aluno = input('')
    alunos.insert(i, aluno)
inversao = alunos[::-1]
print(*inversao, sep='\n')

#Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada
# aluno e imprimí-los na ordem inversa.


