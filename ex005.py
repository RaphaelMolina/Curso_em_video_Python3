limpar = str('\033[m')
texto = {'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'verde2':'\033[36m'}
d = str(' {}Exercício 05{} '.format(texto['vermelho'], limpar))
print('{:=^30}\n'.format(d))

n = int(input('Digite um número: '))
a = int(n - 1)
s = int(n + 1)
print('\nO número digitado foi o {}{}{}.\nSeu antecessor é o {}{}{}.\nE seu sucessor é o {}{}{}.\n'.format(texto['roxo'], n, limpar, texto['verde2'], (n - 1), limpar, texto['vermelho'], (n + 1), limpar))
# Ou
print('Analisando o valor {}{}{}.\nSeu antecessor é {}{}{}.\nE o sucessor é {}{}{}.'.format(texto['verde2'], n, limpar, texto['vermelho'], a, limpar, texto['roxo'], s, limpar))

