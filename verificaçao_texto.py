from time import sleep
texto = input('Diga-me um texto para que eu possa fazer a verificação do mesmo.')
n1 = int(input('Digite o primeiro número a se tornar o índice'))
n2 = int(input('Digite o segundo número a se tornar o índice'))
if n1 > n2:
    n3 = n2
    n2 = n1
    n1 = n3
if n2 > len(texto):
    print('Erro, o número de índice não pode ser maior que o texto!')
else:
    print('Estou verificando, um minuto e te retorno, os valores correspondentes...')
    time.sleep(3)
    print('Partes')
    print(f'Parte 1: {texto[:n1]}')
    print(f'Parte 2: {texto[:n2]}')
    print(f'Parte 3: {texto[n1:n2]}')
    print(f'Parte 4: {texto[n1:-1]}')
    print(f'Parte 5: {texto[n2:-1]}')

# O programa acima, pede ao usuário um texto e retorna partes do texto de acordo com dois índices definidios pelo user.
