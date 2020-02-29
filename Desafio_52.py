from Titulo import Titulo

d = Titulo(52, 'Números primos!!!')
d.Desafio()

n = int(input('Digite um número: '))
t = int()

for contador in range(1, n + 1):
    if n % contador == 0:
        print('\033[34m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
print('\n\n\033[mO número {} foi divisível {} vezes.'.format(n, t))
if t == 2:
    print('E por isso ele é primo!!!')
else:
    print('E por isso ele não é primo!')
