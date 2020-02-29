from datetime import date
from Titulo import Titulo

d = Titulo(54, 'Grupo da Maioridade!!!')
d.Desafio()
totalma = int()
totalme = int()
atual = date.today().year
for contador in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa Nasceu? '.format(contador)))
    idade = atual - nascimento
    if idade >= 21:
        totalma += 1
    else:
        totalme += 1
print('\nAo todo tivemos {} pessoas Maior de idade.'.format(totalma))
print('E também tivemos {} pessoas Menor de idade.'.format(totalme))

