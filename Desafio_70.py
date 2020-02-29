from Titulo import Titulo

d = Titulo(70, 'Estatísticas em produtos!!!')
d.Desafio()
menor = total = float()
maior = contador = int()
barato = str()
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    contador += 1
    if preco > 1000:
        maior += 1

    if contador == 1 or preco < menor:
        menor = preco
        barato = produto

    resposta = str(' ')
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break


print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Temos {maior} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi {barato}, que custa R$ {menor:.2f}.')
