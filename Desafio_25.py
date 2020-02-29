d = str(' Desafio 25 ')
print('{:=^30}\n'.format(d))

nome = str(input('Digite seu nome completo para a verificação: '))
print('\nO nome digitado contém o nome Silva?\n{}'.format('silva' in nome.lower()))
print('\nTrue = Sim / False = Não.')