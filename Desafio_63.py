from Titulo import Titulo

d = Titulo(63, 'Sequência Fibonacci!!!')
d.Desafio()
print('-=' * 15)
print('Sequência de Fibonacci.')
print('-=' * 15)
n = int(input('Quantos termos você quer mostrar? '))

termo1 = int()
termo2 = int(1)

print('-~' * 15)
print(f'{termo1} → {termo2}', end='')

contador = int(3)

while contador <= n:
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' → Fim!')
print('-~' * 15)
