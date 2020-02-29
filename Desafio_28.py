import random
d = str(' Desafio 28 ')
print('{:=^30}\n'.format(d))
print('Jogo da Adivinhação')
numero = int(random.randint(0, 5))
print('\nO computador acabou de pensar em um número inteiro de 0 a 5 adivinhe qual é!')
print(numero)
resposta = int(input('Diga em qual número o computador pensou: '))
if numero == resposta:
    print('\nResposta correta, você acertou.\nParabéns!')
else:
    print('\nResponta errada, você não acertou.\nTente novamente!')

