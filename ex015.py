e = str(' Exercício 15 ')
print('{:=^30}\n'.format(e))

dias = int(input('Por quantos dias você utilizou o carro: '))
km = float(input('Informe o total que Km rodados: '))
valor_dias = int(dias * 60)
valor_km = float(km * 0.15)
valor_total = float(valor_dias + valor_km)
valor_total2 = float((dias * 60) + (km * 0.15))
print('\nO valor total a pagar é de R${:.2f}.'.format(valor_total))
print('\n{:.2f}'.format(valor_total2))

