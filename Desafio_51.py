from Titulo import Titulo

d = Titulo(51, 'Progressão Aritmética!!!')
d.Desafio()

primeiro = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))
décimo = primeiro + 10 * razão

for contador in range(primeiro, décimo, razão):
    print('{} '.format(contador), end='→ ')
print('Fim!')

'''Alt + 24 = ↑, Alt + 25 = ↓, Alt + 23 = ↨, Alt + 26 = →, Alt + 27 = ←,
 Alt + 29 = ↔, Alt + 0171 = «, Alt + 0187 = » '''
