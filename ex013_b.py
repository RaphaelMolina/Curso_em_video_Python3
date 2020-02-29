e = str(' Exercício 13B ')
print('{:=^30}\n'.format(e))

valor_do_produto = float(input('Informe o valor do produto: R$'))
valor_a_vista = float(valor_do_produto - (valor_do_produto * 10 /100))
valor_parcelado = float(valor_do_produto + (valor_do_produto * 8 /100))
print('\nO valor do produto informado é de R${:.2f}.\nEste produto a vista tem 10% de desconto.\nValor a vista R${:.2f}.\nEste produto parcelado tem um pequeno aumento de 8%.\nValor do produto parcelado R${:.2f}.'.format(valor_do_produto, valor_a_vista, valor_parcelado))