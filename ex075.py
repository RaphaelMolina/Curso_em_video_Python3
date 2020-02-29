from Titulo import Titulo

e = Titulo(75, 'Informando valores para a Tupla!!!')
e.Exercicio()
par = tres = nove = contador = n1 = n2 = n3 = n4 = int()

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla = (n1, n2, n3, n4)

print('\nVocê digitou os valores: ', end='')
for numeros in tupla:

    if numeros == 3:
        tres = tupla.index(3) + 1

    if numeros == 9:
        nove += 1

    if contador == 3:
        print(f'{numeros}.')
    else:
        print(numeros, end=', ')
    contador += 1

if nove == 0:
    print('O valor 9 não apareceu!')
elif nove == 1:
    print('O valor 9 apareceu uma vez!')
else:
    print(f'O valor 9 apareceu {nove} vezes!')

if tres == 0:
    print('O valor 3 não foi encontrado nesta tupla!')
else:
    print(f'O valor 3 está na {tres}º posição!')

print('Os valores pares digitados foram: ', end='')
for numeros in tupla:
    if numeros % 2 == 0:
        print(numeros, end=' ')
