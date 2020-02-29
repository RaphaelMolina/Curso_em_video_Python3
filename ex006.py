limpar = str('\033[m')
texto = {'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'verde2':'\033[36m'}
e = str(' {}Exercício 06 {}'.format(texto['vermelho'], texto['verde2']))
print('{}{:=^30}{}\n'.format(texto['verde2'], e, limpar))

n = float(input('{}Didite um número:{} '.format(texto['roxo'], limpar)))
d = float(n*2)
t = float(n*3)
r = float(n**0.5)
# Ou
d1 = n*2
t1 = n*3
r1 = n**0.5
r2 = n**(1/2)
r3 = pow(n, (1/2))
r4 = pow(n, 0.5)

print('\nO dobro de {}{}{}, é {}{}{}.\nO triplo de {}{}{}, é {}{}{}.\nA raiz quadrada de {}{}{}, é {}{:.2f}{}.\n'
      .format(texto['vermelho'], n, limpar, texto['roxo'], d, limpar, texto['verde2'], n, limpar, texto['vermelho'],
              t, limpar, texto['roxo'], n, limpar, texto['verde2'], r, limpar))
print(d1, t1, r1)
print(r2, r3, r4)


