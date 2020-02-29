from Titulo import Titulo
from time import sleep
d = Titulo(59, 'Criando um Menu de Opções!!!')
d.Desafio()

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = int()

while opção != 5:
    print('''\n    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('\n>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'O resultado de {n1} X {n2} é {multiplicação}.')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}.')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(3)
print('\nFim do programa! Volte sempre!')
