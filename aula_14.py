from Titulo import Titulo
a = Titulo(14, 'Estrututa de repetição: While!!!')
a.Aula()
#Estrutura de repetição com teste lógico!

for c in range(1, 10):
    print(c)
print('Fim!')

c = int(1)
while c < 10:
    print(c)
    c += 1
print('Fim!')
p = i = int()
n = int(1)
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print('Você digitou {} números pares e {} números ímpares.'.format(p, i))
print('Fim!')

r = str('S')
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S / N]? ')).upper()
print('Fim!')






