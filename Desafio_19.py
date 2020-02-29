import random
d = str(' Desafio 19 ')
print('{:=^30}\n'.format(d))

aluno1 = str('João')
aluno2 = str('Pedro')
aluno3 = str('José')
aluno4 = str('Thiago')
sorteado = random.choice([aluno1, aluno2, aluno3, aluno4])
print(sorteado)
# Ou
print(random.choice(['João', 'Pedro', 'José', 'Thiago']))




