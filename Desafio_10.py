d = str(' Desafio 10 ')
print('{:=^30}\n'.format(d))

v = float(input('Informe o valor que você tem em sua carteira: R$ '))
d = float(input('Informe a cotação atual do Dólar - 1 Dólar = R$ '))
c = float(v/d)
print('Você pode comprar ${} Dólares.'.format(c))
