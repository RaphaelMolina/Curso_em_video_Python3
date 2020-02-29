d = str(' Desafio 32 ')
print('{:=^30}\n'.format(d))
print('Verificação de ano Bissexto.\n')
ano = int(input('Informe um ano: '))
ano100 = ano % 100
ano400 = ano % 400
ano4 = ano % 4
if ano100 > 0 and ano4 ==0:
    print('\nEste ano é Bissexto!')
else:
    if ano400 == 0:
        print('\nEste ano é Bissexto!')
    else:
        print('\nEste ano não é Bissexto!')


