d = str(' Desafio 22 ')
print('{:=^30}\n'.format(d))

nome = str(input('Informe seu nome completo: '))
nome_dividido = nome.split()
print('\nO nome informado com todas as letras maiúsculas: {}'.format(nome.upper()))

print('\nO nome informado com todas as letras minúsculas: {}'.format(nome.lower()))

print('\nO nome informado tem {} letras'.format(len(nome.replace(' ', ''))))

print('\nO primeiro nome informado é {}, e tem {} letras'.format(nome_dividido[0], len(nome_dividido[0])))
