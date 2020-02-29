from random import randint
from time import sleep
d = str(' Desafio 45 ')
print(f'\n{d:=^50}')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''\nSuas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')

jogador = int(input('\nQual é a sua jogada? '))

print('\nJo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')

print('\nO Computador jogou {}.'.format(itens[computador]))
print('E você jogou {}.'.format(itens[jogador]))

if computador == 0:    # O computador jogou Pedra.
    if jogador == 0:   # O jogador jogou Pedra.
        print('\nEmpatou!!!')
    elif jogador == 1: # O jogador jogou Papel.
        print('\nVocê ganhou!!! Parabéns!!!')
    elif jogador == 2: # O jogador jogou Tesoura.
        print('\nQue pena, você perdeu!')
    else:
        print('\n\033[31mJogada inválida.\nTente novamente\033[m!!!')
elif computador == 1:  # O computador jogou Papel.
    if jogador == 0:   # O jogador jogou Pedra.
        print('\nQue pena, você perdeu!')
    elif jogador == 1: # O jogador jogou Papel.
        print('\nEmpatou!!!')
    elif jogador == 2: # O jogador jogou Tesoura.
        print('\nVocê ganhou!!! Parabéns!!!')
    else:
        print('\n\033[31mJogada inválida.\nTente novamente\033[m!!!')
elif computador == 2:  # O computador jogou Tesoura.
    if jogador == 0:   # O jogador jogou Pedra.
        print('\nVocê ganhou!!! Parabéns!!!')
    elif jogador == 1: # O jogador jogou Papel.
        print('\nQue pena, você perdeu!')
    elif jogador == 2: # O jogador jogou Tesoura.
        print('\nEmpatou!!!')
    else:
        print('\n\033[31mJogada inválida.\nTente novamente\033[m!!!')
