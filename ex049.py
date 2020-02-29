from Titulo import Titulo
e = Titulo(49, 'Tabuada!!!')
e.Exercicio()

n = int(input('Informe um número para ter acesso a sua Tabuada: '))

print(f'\nTabuada do {n}')
for contador in range(1, 11):
    r = contador * n
    print(f'{n} x {contador} = {r}')


