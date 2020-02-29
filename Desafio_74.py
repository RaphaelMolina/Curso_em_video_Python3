from Titulo import Titulo
from random import randint
d = Titulo(74, 'Maior e menor valores em Tupla!!!')
d.Desafio()

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
# função max() retorna o maior valor.
# função min() retorna o menor valor.
print(f'\nO maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')
