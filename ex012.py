e = str(' Exercício 12 ')
print('{:=^30}\n'.format(e))

preco = float(input('Informe o valor do produto para calcular o desconto: R$ '))
desconto = float(preco * 0.05)
desconto2 = float(preco * 5 / 100)
novo_preco = float(preco - desconto)
novo_preco2 = float(preco - desconto2)
novo_preco3 = float(preco - (preco * 5 / 100))

print('\nO produto que custava R${:.2f}. Na promoção com o desconto de 5%, vai custar agora R${:.2f}.'.format(preco,
                                                                                                              novo_preco))
print('\n', novo_preco, '\n', novo_preco2, '\n', novo_preco3)
