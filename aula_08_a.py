import math # Importando a biblioteca de matemática
from math import sqrt # importando uma função especifica da biblioteca de matemática, função de raiz quadrada
from math import ceil # importando uma função especifica da biblioteca de matemática, função de arredondamento para cima
from math import floor # importando uma função especifica da biblioteca de matemática, função de arredondamento para baixo
# Ou from math import sqrt, ceil, floor (Irá importar várias funções especificas da biblioteca de matemática)
aula = str(' Aula 08 ')
print('{:=^30}\n'.format(aula))

numero = int(input('Digite umm número: '))
raiz = math.sqrt(numero)
raiz2 = sqrt(numero)

print('A raiz de {} é igual a {}'.format(numero, raiz))
print('Raiz arredondada para cima {}'.format(math.ceil(raiz)))
print('Raiz arredondada para baixo {}'.format(math.floor(raiz)))
print('Raiz arredondada com 2 casas decimais (duas casas após o ponto flutuante) {:.2f}'.format(raiz))
print(raiz2)
print(ceil(raiz2))
print(floor(raiz2))

