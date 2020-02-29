e = str(' Exercício 34 ')
print('{:=^30}\n'.format(e))
print('Calculando seu novo salário com aumento.\n')
salario = float(input('Informe seu salário atual: R$'))
if salario <= 1250:
    aumento = str('15%')
    novo_salario = (salario * 0.15) + salario
    novo_salario1 = salario + (salario * 15 / 100)
else:
    aumento = str('10%')
    novo_salario = (salario * 0.10) + salario
    novo_salario1 = salario + (salario * 10 / 100)
print('\nSeu Salário de R${:.2f}, terá um aumento de {}.\nSeu novo Salário será R${:.2f}'.format(salario, aumento, novo_salario))
print('\nSeu Salário de R${:.2f}, terá um aumento de {}.\nSeu novo Salário será R${:.2f}'.format(salario, aumento, novo_salario1))


