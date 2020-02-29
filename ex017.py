import math
e = str(' Exercício 17 ')
print('{:=^30}\n'.format(e))

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('A hipotenusa dos catetos informado é de: {:.2f}'.format(hipotenusa))
hipotenusa2 = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa dos catetos informado é de: {:.2f}'.format(hipotenusa2))

