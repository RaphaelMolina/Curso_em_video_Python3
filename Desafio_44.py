d = str(' Desafio 44 ')
print(f'\n{d:=^50}')

print('\n{:=^50}'.format(d))

preço = float(input('\nPreço das compras: R$'))
print('''\nFormas de pagamento:
[ 1 ] Á vista no dinheiro ou cheque.
[ 2 ] Á vista no cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.
''')
opção = int(input('Qual é a opção? '))
print('')

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}, sem juros!'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print('\nSua compra será parcelada em {}x de {:.2f}, com juros!'.format(parcelas, parcela))
else:
    total = preço
    print('''\033[31mOpção inválida de pagamento.
Tente novamente!!!\033[m\n''')

print('Sua compra de R${:.2f}, vai custar R${:.2f} no final.'.format(preço, total))
