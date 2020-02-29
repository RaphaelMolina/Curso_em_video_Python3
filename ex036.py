e = str('Exercício 36')
print('\n \033[31m{:=<15}\033[m \033[35m{}\033[m \033[34m{:=>15}\033[m'.format('', e, ''))

print('\n \033[32mAprovação de empréstimo bancário!\033[m')
print('\n \033[4mVamos verificar os seus dados.\033[m')

casa = float(input('\nInforme o valor do imóvel: '))
salario = float(input('Informe o valor da sua renda R$ '))
anos = int(input('Informe em quantos anos deseja pagar este imóvel: '))
meses = int(12 * anos)
prestação = float(casa / meses)

if prestação > salario * 0.30:
    print('\nEmpréstimo Negado!!!')
    print('O valor da prestação excede o limite permitido que é de R${:.2f}.'.format(salario * 0.30))
else:
    print('\nSeu imóvel no valor de R${:.2f}, terá {} prestações de R${:.2f}.'. format(casa, meses, prestação))



