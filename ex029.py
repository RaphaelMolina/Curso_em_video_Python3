e = str(' Exercício 29 ')
print('{:=^30}\n'.format(e))
print('Sistema verificador de multa com base em sua velocidade.\n')
velocidade = float(input('Qual é a velocidade do seu carro? '))
if velocidade > 80:
    print('\nVocê foi Multado!\nVocê excedeu o limite permitido de 80km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}.'.format(multa))
print('\nTenha um bom dia!\nDirija com segurança!')

