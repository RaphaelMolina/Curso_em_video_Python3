from datetime import date
e = str(' Exercício 32 ')
print('{:=^30}\n'.format(e))
print('Verificando se o ano é Bissexto ou não.\n')
print('Digite 0 para verificar o ano atual.\n')
ano = int(input('Informe o ano para ser verificado: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} é Bissexto!'.format(ano))
else:
    print('\nO ano {} não é Bissexto!'.format(ano))

