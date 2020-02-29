import random
d = str(' Desafio 20 ')
print('{:=^30}\n'.format(d))

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
selecao = random.sample((aluno1, aluno2, aluno3, aluno4), k=4)
print('\nSorteio para Apresentação\n')
print('Ordem da Apresentação:{}.'.format(selecao))
