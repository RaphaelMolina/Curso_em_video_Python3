from Titulo import Titulo

e = Titulo(64, 'Soma dos números informados!!!')
e.Exercicio()

total = contador = n = int()

while n != 999:
    n = int(input('Informe um número: '))
    if n != 999:
        total += n
        contador += 1
print(f'\nForam digitados {contador} números.'
      f'\nO resultado da soma entre os números informados é {total}.')
print('\nFim!')
