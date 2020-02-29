e = str(' Exercício 13 ')
print('{:=^30}\n'.format(e))

salario = float(input('Qual é o seu salário? R$ '))
novo_salario = float(salario + (salario * 15 / 100))
print('\nUm funcionário que ganhava R${:.2f}, com um aumento de 15%, passa a receber R${:.2f}'.format(salario, novo_salario))
