from Titulo import Titulo

e = Titulo(50, 'Soma dos números pares!!!')
e.Exercicio()
print('Informe Seis números\n')
r = int()
for contador in range(1, 7):
    n = int(input(f'Informe o {contador}º número: '))
    if n % 2 == 0:
        r += n
print(f'\nA soma de todos os números pares é igual a {r}')
