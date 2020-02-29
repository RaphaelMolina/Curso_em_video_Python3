from Titulo import Titulo
from time import sleep

e = Titulo(59, 'Menu de operações!!!')
e.Exercicio()

r = opção = n1 = n2 = int()

while opção != 5:
    print('Informe 2 números e escolha a opção que desejar:')
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    print('\nMenu de operações:')
    opção = int(input('Digite [ 1 ] para somar.\n'
                      'Digite [ 2 ] para multiplicar.\n'
                      'Digite [ 3 ] para verificar qual é o maior.\n'
                      'Didite [ 4 ] para escolher novos números.\n'
                      'Ou digite [ 5 ] para sair do programa.\n'
                      '\nO que você deseja fazer? '))
    if opção == 1:
        r = n1 + n2
        print(f'\nO resultado entre a soma de {n1} e {n2} é {r}.\n')
    elif opção == 2:
        r = n1 * n2
        print(f'\nO resultado entre a multiplicação de {n1} e {n2} é {r}.\n')
    elif opção == 3:
        if n1 > n2:
            r = n1
            print(f'\nO maior número entre {n1} e {n2} é {r}.\n')
        elif n1 == n2:
            print(f'\nNão há um número maior entre {n1} e {n2} eles são iguais.\n')
        else:
            r = n2
            print(f'\nO maior número entre {n1} e {n2} é {r}.\n')
    elif opção == 4:
        print('\nReiniciando...\n')
        sleep(5)
print('\nPrograma encerrado.')