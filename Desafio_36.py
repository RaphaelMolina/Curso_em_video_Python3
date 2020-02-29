d = str(' Desafio 36 ')
print(f'\n{d:=^50}')

casa = float(input('\nValor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestação = casa / (anos * 12)

mínimo = salário * 0.30
minimo = salário * (30 / 100)
minimo1 = salário * 30 / 100

print('\nPara pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(prestação))

if prestação <= mínimo:
    print('O empréstimo pode ser concedido!')
else:
    print('Empréstimo Negado!')

