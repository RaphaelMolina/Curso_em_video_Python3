d = str(' Desafio 11 ')
print('{:=^30}\n'.format(d))

l = float(input('Informe a Largura de sua parede em metros: '))
al = float(input('Informe a Altura de sua parede em metros: '))
ar = float(l*al)
t = float(ar/2)

print('Sua parede tem {} metros quadrados'.format(ar))
print('Será necessário {} Litros de tinta para pintá-la.'.format(t))

