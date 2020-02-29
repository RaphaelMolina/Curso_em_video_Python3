from Titulo import Titulo

e = Titulo(63, 'Sequência de Fibonacci!!!')
e.Exercicio()
contador = n2 = n1 = sequencia = int()
n = int(input('Quantos elementos da sequência de Fibonacci você deseja ver? '))
n2 = 1
print('')
while contador < n:
    print(f'{sequencia}', end=' → ')

    if contador % 2 == 0:
        n1 = sequencia
    elif contador % 2 != 0:
        n2 = sequencia

    contador += 1

    sequencia = n1 + n2

print('Fim!')
