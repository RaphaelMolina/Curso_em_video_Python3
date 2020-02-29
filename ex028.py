from random import randint
from time import sleep
from emoji import emojize
e = str(' Exercício 28 ')
print('{:=^30}\n'.format(e))
print('**==' * 15)
print('{:^60}'.format('Jogo da Adivinhação!'))
print('{:^60}'.format('Adivinhe em qual número de 0 a 5 o computador pensou.'))
print('**==' * 15)
sleep(5)
computador = randint(0, 5) # Irá escolher um número aleatório entre 0 e 5.
print('\nEstou pensando...')
sleep(5)
print('Pronto!')
jogador = int(input('\nEm qual número o computador pensou? '))
print('Verificando...')
sleep(5)

if jogador == computador:
    print(emojize('\n:tada: :confetti_ball: Parabéns!!! :tada: :confetti_ball:', use_aliases=True))
    print(emojize(':smile: Você Ganhou! :smile:', use_aliases=True))
else:
    print(emojize('\n:cry: Que pena, Você perdeu! :cry:', use_aliases=True))
    print('O computador pensou no número {} e você pensou no número {}.'.format(computador, jogador))
