from Titulo import Titulo

d = Titulo(75, 'Análise de dados em uma Tupla!!!')
d.Desafio()
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'\nVocê digitou os valores: {numeros}')

# A função count() irá apresentar quantos ocorrências do
# parâmetro informado tiveram na tupla.

print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
