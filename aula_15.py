from Titulo import Titulo

a = Titulo(15, 'Interrompendo repetições while!!!')
a.Aula()

contador = int(1)

while contador <= 10:
    print(contador, ' → ', end='')
    contador += 1
print('Acabou!')

soma = contador = n = int()
while contador < 3:
    n = int(input('Digite um número: '))
    contador += 1

while n != 999:
    n = int(input('Digite um número: '))
    soma += n
print(f'A soma vale {soma}.')

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}.')

nome = str('Raphael')
idade = int(30)

print('\nO %s tem %d anos.' % (nome, idade)) # Python 2
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print(f'O {nome} tem {idade} anos.') # Python 3.6+
