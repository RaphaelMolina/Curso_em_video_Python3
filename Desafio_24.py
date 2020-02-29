d = str(' Desafio 24 ')
print('{:=^30}\n'.format(d))

cidade = str(input('Informe o nome de uma Cidade: '))
dividir = cidade.split()
print('\nO nome da Cidade começa com a palavra Santo?\n{}'.format('santo' in dividir[0].lower()))
print('\nTrue = Sim / False = Não.')
