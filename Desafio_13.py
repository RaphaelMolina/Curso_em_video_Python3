d = str(' Desafio 13 ')
print('{:=^30}\n'.format(d))

s = float(input('Informe o seu salário para calcular o aumento: R$ '))
a = float(s*0.15)
ns = float(s+a)
print('Você teve um aumento de 15% em seu salário!\nSeu novo salário já com aumento é de: R$ {}'.format(ns))
