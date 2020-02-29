e = str(' Exercício 27 ')
print('{:=^30}\n'.format(e))

nome_completo = str(input('Digite seu nome completo: ')).strip()
nome = nome_completo.split()
print('\nMuito prazer em te conhecer!\n{}.'.format(nome_completo))
print('\nSeu primeiro nome é {}.'.format(nome_completo.split()[0]))
print('Seu último nome é {}.'.format(nome_completo.rsplit()[-1:]))
print('Seu último nome é {}.'.format(nome[len(nome) - 1]))
