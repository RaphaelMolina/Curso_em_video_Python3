from Titulo import Titulo

d = Titulo(55, 'Maior e o menor da sequência!!!')
d.Desafio()

maior = float()
menor = float()

for contador in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(contador)))
    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nO maior peso lido foi {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))

