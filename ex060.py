from Titulo import Titulo

e = Titulo(60, 'Fatorial de um número!!!')
e.Exercicio()
c = r = n = int()
n = int(input('Informe um número: '))
c = n - 1

while c != 0:
    if r == 0:
        r = n * c
    else:
        r *= c
    c -= 1
print(f'\nO Fatorial do número {n} é {r}.')

c = n - 1
r = 0

for contador in range(c, 0, -1):
    if r == 0:
        r = n * contador
    else:
        r *= contador
print(f'\nO Fatorial do número {n} é {r}.')

