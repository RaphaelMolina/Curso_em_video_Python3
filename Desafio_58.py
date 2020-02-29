from Titulo import Titulo
from random import randint

d = Titulo(58, 'Jogo da Adivinhação!!!')
d.Desafio()

computador = randint(0, 10)
palpites = int()
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False

while not acertou:
    jogador = int(input('\nQual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'\nAcertou com {palpites} tentativas. Parabéns!')


