import random
e = str(' Exercício 20 ')
print('{:=^30}\n'.format(e))

print('Sorteio para a apresentação dos trabalhos\n')
primeiro_aluno = str(input('Informe o nome do primeiro aluno: '))
segundo_aluno = str(input('Informe o nome do segundo aluno: '))
terceiro_aluno = str(input('Informe o nome do terceiro aluno: '))
quarto_aluno = str(input('Informe o nome do quarto aluno: '))
lista_de_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(lista_de_alunos)
print('\nA ordem de apresentação será \n{}'.format(lista_de_alunos))
