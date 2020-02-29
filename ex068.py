from Titulo import Titulo
from random import randint
e = Titulo(68, 'Par ou Ímpar!!!')
e.Exercicio()

print('=-' * 30)
print('Vamos Jogar Par ou ímpar!')
total = contador = int()
while True:
    computador = randint(0, 10)
    print('-=' * 30)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        print('-' * 60)
        print('Desculpe não entendi sua escolha.')
        print('Digite P para Par e I para Ímpar.')
        print('-' * 60)
        escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    total = computador + jogador
    if total % 2 == 0:
        jogada = str('Par')
    else:
        jogada = str('Ìmpar')
    print('=' * 60)
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'O Total deu {total} que é {jogada}.')
    print('=' * 60)
    if escolha == 'P' and jogada == 'Par' or escolha == 'I' and jogada == 'Ìmpar':
        contador += 1
        print('Você Venceu!')
        print('Vamos jogar novamente...')
    else:
        print('Você perdeu!')
        if contador == 0:
            print('Game Over! Você não venceu nenhuma vez.')
        if contador == 1:
            print(f'Game Over! Você venceu {contador} vez.')
        if contador > 1:
            print(f'Game Over! Você venceu {contador} vezes.')
        break
