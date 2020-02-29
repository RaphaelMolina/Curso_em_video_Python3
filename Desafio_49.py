from Titulo import Titulo

d = Titulo(49, 'Tabuada!!!')
d.Desafio()
n = int(input('Digite um número para ver a sua Tabuada: '))

for contador in range(1, 11):
    print('{} X {:2} = {}'.format(n, contador, n * contador))
