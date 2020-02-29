import math
d = str(' Desafio 16 ')
print('{:=^30}\n'.format(d))
'''Esta é a forma para
Comentar várias linhas'''

numero = float(input('Digite um número real com ponto flutuante: '))

print('A porção inteira do número informado é {}'.format(int(numero)))
print('A porção inteira dp número informado é {}'.format(math.floor(numero))) # Certo
print('A porção inteira do número informado é {}'.format(math.trunc(numero))) # O método Trunc utiliza somente a parte inteira de um número