from Titulo import Titulo

d = Titulo(65, 'Maior e Menor valores!!!')
d.Desafio()

resposta = str('S')
menor = maior = quantidade = soma = media = int()
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / quantidade

print(f'\nVocê digitou {quantidade} números e a média foi {media}.')
print(f'O Maior valor foi {maior} e o Menor valor foi {menor}.')
