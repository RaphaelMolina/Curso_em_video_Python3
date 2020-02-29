import math
e = str(' Exercício 16 ')
print('{:=^30}\n'.format(e))
valor = float(input('Digite um valor: '))
print('O valor digitado foi {}. E a sua porção inteira é {}'.format(valor, math.floor(valor)))
print('Ou {}'.format(math.trunc(valor)))
