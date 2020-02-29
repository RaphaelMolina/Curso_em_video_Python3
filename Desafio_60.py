from Titulo import Titulo
from math import factorial

d = Titulo(60, 'Cálculo do Fatorial!!!')
d.Desafio()

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'\nO Fatorial de {n}! é {f}.')

fatorial = int(1)
contador = n
print(f'\nCalculando {n}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' X ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}.')

print('\nFim!\n')

fatorial = 1
print(f'Calculando {n}! = ', end='')
for contador in range(n, 0, -1):
    print(f'{contador}', end='')
    print(' X ' if contador > 1 else ' = ', end='')
    fatorial *= contador
print(f'{fatorial}.')
