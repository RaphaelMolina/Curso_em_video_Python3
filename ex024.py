e = str(' Exercício 24 ')
print('{:=^30}\n'.format(e))

cidade = str(input('Digite o nome da Cidade em que você nasceu: ')).strip().lower()
print('\nA Cidade em que você nasceu começa com a palavra Santo? {}'.format(cidade[0:5] == 'santo'))
print('\nTrue = Sim / False = Não')