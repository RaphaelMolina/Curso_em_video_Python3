d = str(' Desafio 27 ')
print('{:=^30}\n'.format(d))

nome_completo = str(input('Digite seu nome completo: '))

print('\nO nome digitado foi: {}'.format(nome_completo))
print('O primeiro nome é: {}'.format(nome_completo.split()[0]))
print('O último nome é: {}'.format(nome_completo.rsplit()[-1:]))
