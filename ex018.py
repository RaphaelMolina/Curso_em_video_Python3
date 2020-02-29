import math

e = str(' Exercício 18 ')
print('{:=^30}\n'.format(e))

angulo = float(input('Digite um ângulo para que seja calculado o Seno, Cosseno e Tangente: '))
seno = float(math.sin(math.radians(angulo)))
cosseno = float(math.cos(math.radians(angulo)))
tangente = float(math.tan(math.radians(angulo)))
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))
