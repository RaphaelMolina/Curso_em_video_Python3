d = str(' Desafio 23 ')
print('{:=^30}\n'.format(d))

numero = str(input('Digite um número de 0 a 9999: '))

print('\nO número digitado tem:\n')
print('unidade: {}'.format(numero[3]))
print('dezena:  {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar:  {}'.format(numero[0]))

