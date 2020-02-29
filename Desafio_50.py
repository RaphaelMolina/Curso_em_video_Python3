from Titulo import Titulo

d = Titulo(50, 'Soma dos pares!!!')
d.Desafio()

soma = int()
cont = int()

for contador in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(contador)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('\nVocê informou {} números pares e a soma foi {}.'.format(cont, soma))
