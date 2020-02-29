from Titulo import Titulo

e = Titulo(52, 'Verificador de Número Primo!!!')
e.Exercicio()

n = int(input('Informe um número: '))
a = int()
for contador in range(1, n+1):
    if n % contador == 0:
        a += 1

if a == 2:
    print(f'\n\33[34mO número {n} é primo!!\33[m')
else:
    print(f'\n\33[31mO número {n} não é primo!\33[m')

