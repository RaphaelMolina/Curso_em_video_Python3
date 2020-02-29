from Titulo import Titulo

e = Titulo(70, "Nome e valor dos Produtos!!!")
e.Exercicio()

menor = total = float()
contador = maior = int()
barato = str()

print('-' * 30)
print(' ' * 5, 'Loja Super Baratão', ' ' * 5)
print('-' * 30)

while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$ '))
    if valor > 1000:
        maior += 1

    if contador == 0:
        menor = valor
        barato = nome
    elif valor < menor:
        menor = valor
        barato = nome
    contador += 1
    total += valor
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        print('-' * 15, 'Fim do Programa', '-' * 15)
        print(f'O Total da compra foi de R$ {total:.2f}.')
        if maior == 0:
            print('Não tivemos nenhum pruduto custando mais do que R$ 1.000,00.')
        if maior == 1:
            print('Temos apenas um produto custando mais do que R$ 1.000,00.')
        else:
            print(f'Temos {maior} produtos custando mais do que R$ 1.000,00.')
        print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}.')
        break
