d = str(' Desafio 29 ')
print('{:=^30}\n'.format(d))
print('Verificador de Multas\n')
velocidade = float(input('Informe a velocidade do veículo em km por hora: '))
multa = float((velocidade - 80.00) * 7.00)
if velocidade > 80.00:
    print('\nSeu veículo foi Multado!\nO valor Total da Multa é de: R$ {:.2f}'.format(multa))
else:
    print('Não há multas para seu veículo')

