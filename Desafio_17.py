import math
d = str(' Desafio 17 ')
print('{:=^30}\n'.format(d))

cateto_oposto = float(input('Informe o comprimento do cateto oposto de um triângulo retângulo: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente de um triângulo retângulo: '))
hipotenusa = float((cateto_oposto**2 + cateto_adjacente**2)**0.5)# Calculando a Hipotenusa com fórmula

print('A Hipotenusa do triângulo retângulo é = {:.2f}'.format(hipotenusa))
print('A Hipotenusa do triângulo retângulo é = {:.2f}'.format(math.hypot(cateto_oposto, cateto_adjacente)))# Calculando a Hipotenusa com um método
