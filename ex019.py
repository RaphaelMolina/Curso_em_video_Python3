import random
e = str(' Exercício 19 ')
print('{:=^30}\n'.format(e))

print('Sorteio para apagar a lousa\n')
primeiro_aluno = str(input('Informe o nome do primeiro aluno: '))
segundo_aluno = str(input('Informe o nome do segundo aluno: '))
terceiro_aluno = str(input('Informe o nome do terceiro aluno: '))
quarto_aluno = str(input('Informe o nome do quarto aluno: '))
lista_de_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
escolha = random.choice(lista_de_alunos)
print('\nO aluno escolhido foi aluno(a): {}'.format(escolha))
