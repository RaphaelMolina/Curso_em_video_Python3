from Titulo import Titulo
from random import randint

d = Titulo(68, 'Jogo do Par ou Ímpar!!!')
d.Desafio()
contador = int()
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = str(' ')
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {contador} vezes.')
