text_1 = input('Texto 1?')
text_2 = input('Texto 2?')
text_3 = input('Texto 3?')
textos = [text_1.lower(), text_2.lower(), text_3.lower()]
textos.sort()
print('Seguem os textos em ordem:')
print(f'1º {textos[0]}')
print(f'2º {textos[1]}')
print(f'3º {textos[-1]}')

# O programa pede ao usuário 3 palavras e as coloca na ordem alfabética.
