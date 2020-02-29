e = str(' Exercício 31 ')
print('{:=^30}\n'.format(e))
print('Calculando o valor de sua passagem:\n')
viagem = float(input('Qual é a distância de sua viagem em km? '))
print('Você esta prestes a começar uma viagem de {:.2f}km.'.format(viagem))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('\nO preço da sua passagem será de R${:.2f}.'.format(preco))

preco2 = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('\nO preço de sua passagem será de R${:.2f}.'.format(preco2))
