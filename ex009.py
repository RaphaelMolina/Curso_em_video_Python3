limpar = str('\033[m')

texto = {'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'verde2':'\033[36m'}

e = str('{} Exercício 9 {}'.format(texto['vermelho'], texto['verde2']))
print('{}{:=^30}{}\n'.format(texto['verde2'], e, limpar))

t = int(input('{}Digite um número para ver a sua Tabuada: {}'.format(texto['roxo'], limpar)))
a = int(t*1)
b = int(t*2)
c = int(t*3)
d = int(t*4)
e = int(t*5)
f = int(t*6)
g = int(t*7)
h = int(t*8)
i = int(t*9)
j = int(t*10)
l = str('-')
print('\n{}{:-<13}{}'.format(texto['vermelho'], l, limpar))
# Ou print('-' *13)
print('{}{}{} X  {}1{} = {}{}{}'
      '\n{}{}{} X  {}2{} = {}{}{}'
      '\n{}{}{} X  {}3{} = {}{}{}'
      '\n{}{}{} X  {}4{} = {}{}{}'
      '\n{}{}{} X  {}5{} = {}{}{}'
      '\n{}{}{} X  {}6{} = {}{}{}'
      '\n{}{}{} x  {}7{} = {}{}{}'
      '\n{}{}{} X  {}8{} = {}{}{}'
      '\n{}{}{} X  {}9{} = {}{}{}'
      '\n{}{}{} X {}10{} = {}{}{}'
      .format(texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], a, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], b, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], c, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], d, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], e, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], f, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], g, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], h, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], i, limpar,
              texto['vermelho'], t, limpar, texto['verde2'], limpar, texto['roxo'], j, limpar))
print('{}{:-<13}{}'.format(texto['vermelho'], l, limpar))
# Ou print('{} X {:2} = {}'.format(t, 1, t*1))




