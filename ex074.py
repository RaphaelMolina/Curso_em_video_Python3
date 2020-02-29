from Titulo import Titulo
from random import randint

e = Titulo(74, 'Números Aleatórios na tupla!!!')
e.Exercicio()

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
contador = maior = menor = int()

print('Os valores sorteados foram:')
for numeros in tupla:
    if contador == 0:
        maior = menor = numeros
    elif numeros < menor:
        menor = numeros
    elif numeros > maior:
        maior = numeros
    if contador == 4:
        print(f'{numeros}.')
    else:
        print(numeros, end=', ')
    contador += 1
print(f'O Maior valor sorteado foi {maior}.')
print(f'O Menor valor sorteado foi {menor}.')
