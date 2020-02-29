d = str(' Desafio 34 ')
print('{:=^30}\n'.format(d))
print('Calculando o valor de seu aumento salarial')
salario = float(input('Informe o valor de seu salário para calcularmos o aumento: '))
if salario > 1250.00:
    print('\nVocê terá um aumento de 10% em seu salário.')
    print('O valor do aumento é de: R${:.2f}'.format(salario * 0.10))
    print('O valor de seu salário com aumento é de: R${:.2f}'.format((salario * 0.10) + salario))
else:
    print('\nVocê terá um aumento de 15% em seu salário.')
    print('O valor do aumento é de: R${:.2f}'.format(salario * 0.15))
    print('O valor de seu salário com aumento é de: R${:.2f}'.format((salario * 0.15) + salario))
