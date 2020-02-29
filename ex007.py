limpar = str('\033[m')

texto = {'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'verde2':'\033[36m'}

e = str(' {}Exercício 07 {}'.format(texto['vermelho'], texto['verde2']))
print('{}{:=^30}{}\n'.format(texto['verde2'], e, limpar))

n1 = float(input('{}Digite a sua primeira nota:{} '.format(texto['roxo'], limpar)))
n2 = float(input('{}Digite a sua segunda nota:{} '.format(texto['verde2'], limpar)))
m = float((n1+n2)/2)
print('\nA média entre a nota {}{:.1f}{} e {}{:.1f}{} é igual a {}{:.1f}{}.'
      .format(texto['vermelho'], n1, limpar, texto['roxo'], n2, limpar, texto['verde2'], m, limpar))
