import math
d = str(' Desafio 18 ')
print('{:=^30}\n'.format(d))

angulo = float(input('Informe um ângulo em graus: '))
radianos = float(math.radians(angulo))
radianos2 = float(angulo * (3.141592/180))# formula para converter ângulo em graus em ângulo em radianos (ângulo * Pi/180º)
seno = float(math.sin(radianos))
cosseno = float(math.cos(radianos))
tangente = float(math.tan(radianos))
print('O seno do ângulo informado é {}.\nO cosseno do ângulo informado é {}.\nE a tangente do ângulo informado é {}.'.format(seno, cosseno, tangente))
print(radianos)
print(radianos2)


