d = str(' Desafio 31 ')
print('{:=^30}\n'.format(d))

print('Cálculo do valor da passagem.\n')
distancia = float(input('Informe a distância que será percorrida em sua viagem em km: '))
if distancia <= 200.00:
    print('\nO valor da sua passagem é de R$ {:.2f}.'.format(distancia * 0.50))
else:
    print('\nO valor da sua passagem é de R$ {:.2f}.'.format(distancia * 0.45))
