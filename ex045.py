from random import randint
from time import sleep

e = str('Exercício 45')
print(f'\n\033[31m{"=" * 15}\033[m \033[35m{e}\033[m \033[34m{"=" * 15}\033[m')

print(f'\n{" " * 12}\033[4;32mJogo do Jokenpô!!!\033[m')

print('\n\033[4mRegras do Jogo\033[m')
print('Você e o computador irão escolher entre:')
print('\033[31m1 - Pedra\033[m.')
print('\033[34m2 - Papel\033[m.')
print('\033[35m3 - Tesoura\033[m.')
print('\nDigite o número correspondente a sua escolha quando for questionado.')
print('\nPedra vence Tesoura.')
print('Tesoura vence Papel.')
print('Papel vence Pedra.')
print('Se as opções escolhidas forem iguais dará \033[32mEmpate\033[m')

sleep(30)
print('\nVamos lá!!!')
sleep(2)
escolha = int(input('\nE então o que você escolheu? '))
sleep(2)
print('\nJo')
sleep(2)
print('\nKen')
sleep(2)
print('\nPô')

computador = randint(1, 3)

if escolha == 1 and computador == 1:
    print('\nDeu \033[32mempate\033[m!')
    print('Você e o Computador escolheram \033[31mPedra\033[m.')
elif escolha == 1 and computador == 2:
    print('\nVocê perdeu!')
    print('Você escolheu \033[31mPedra\033[m e o Computador escolheu \033[34mPapel\033[m.')
elif escolha == 1 and computador == 3:
    print('\nVocê ganhou!')
    print('Você escolheu \033[31mPedra\033[m e o Computador escolheu \033[35mTesoura\033[m.')
elif escolha == 2 and computador == 2:
    print('\nDeu \033[32mempate\033[m!')
    print('Você e o Computador escolheram \033[34mPapel\033[m.')
elif escolha == 2 and computador == 3:
    print('\nVocê perdeu!')
    print('Você escolheu \033[34mPapel\033[m e o Computador escolheu \033[35mTesoura\033[m.')
elif escolha == 2 and computador == 1:
    print('\nVocê ganhou!')
    print('Você escolheu \033[34mPapel\033[m e o Computador escolheu \033[31mPedra\033[m.')
elif escolha == 3 and computador == 3:
    print('\nDeu \033[32mempate\033[m!')
    print('Você e o Computador escolheram \033[35mTesoura\033[m.')
elif escolha == 3 and computador == 1:
    print('\nVocê perdeu!')
    print('Você escolheu \033[35mTesoura\033[m e o Computador escolheu \033[31mPedra\033[m.')
elif escolha == 3 and computador == 2:
    print('\nVocê ganhou!')
    print('Você escolheu \033[35mTesoura\033[m e o Computador escolheu \033[34mPapel\033[m.')




