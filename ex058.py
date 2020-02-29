from Titulo import Titulo
from random import randint

e = Titulo(58, 'Jogo da Adivinhação!!!')
e.Exercicio()
pc = randint(0, 10)
contador = int()
n = int(11)
print('Adivinhe em qual número de 0 a 10 o computador pensou:\n')
while n != pc:
    n = int(input('Informe seu palpite: '))
    if n != pc:
        print('Você errou, tente novamente.\n')
    contador += 1
print(f'Parabéns você acertou, foram necessário {contador} palpites.')
