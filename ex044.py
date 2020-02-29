e = str('Exercício 44')
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n\033[4;32mVerificando o valor a ser pago pelo produto de acordo com a forma de pagamento!!!\033[m')

preco = float(input('\nInforme o preço do produto: '))

print('\n\033[4mFormas de pagamento disponíveis:\033[m')
print('\033[31m1\033[m - À vista com dinheiro ou cheque.')
print('\033[32m2\033[m - À vista no cartão.')
print('\033[33m3\033[m - Em 2x no cartão.')
print('\033[34m4\033[m - Em 3x ou mais no cartão.')

pagamento = int(input('\nDigite o número correspondente a forma de pagamento que irá realizar: '))

if pagamento == 1:
    print('\nO preço original do produto era \033[35mR${:.2f}\033[m.'.format(preco))
    print('Mas devido a forma de pagamento escolhida você ganhou um desconto de \033[31m10%\033[m!')
    print('O novo preço será de \033[34mR${:.2f}\033[m.'.format(preco - (preco * 0.10)))
elif pagamento == 2:
    print('\nO preço original do produto era \033[35mR${:.2f}\033[m.'.format(preco))
    print('Mas devido a forma de pagamento escolhida você ganhou um desconto de \033[31m5%\033[m!')
    print('O novo preço será de \033[34mR${:.2f}\033[m.'.format(preco - (preco * 0.05)))
elif pagamento == 3:
    print('\nO preço original do produto é \033[35mR${:.2f}\033[m.'.format(preco))
    print('Devido a forma de pagamento escolhida, o preço não teve alteração!')
elif pagamento == 4:
    print('\nO preço original do produto era \033[35mR${:.2f}\033[m.'.format(preco))
    print('Mas devido a forma de pagamento escolhida, o preço teve um acrescimo de \033[31m20%\033[m de juros!')
    print('O novo preço será de \033[34mR${:.2f}\033[m.'.format(preco + (preco * 0.20)))
