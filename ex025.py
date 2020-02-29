e = str(' Exercício 25 ')
print('{:=^30}\n'.format(e))

nome = str(input('Qual seu nome Completo?\n ')).strip().lower()
print('Seu nome tem Silva?\n{}'.format('silva' in nome))
print('\nTrue = Sim / False = Não')
