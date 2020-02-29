from Titulo import Titulo

e = Titulo(61, 'Progressão Aritmética!!!')
e.Exercicio()

t = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
d = int((r * 10) + t)
c = int(1)
print('\nAqui estão os 10 primeiros termos da PA:\n')
while t < d:
    print(f'{c}º Termo → {t}.')
    t += r
    c += 1
print('\nFim!')

