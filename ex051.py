from Titulo import Titulo

e = Titulo(50, 'Progressão Aritmética!!!')
e.Exercicio()

t = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
print('\nAqui estão os 10 primeiros termos da PA:')
for contador in range(t, (10*r) + t, r):
    print(contador)
