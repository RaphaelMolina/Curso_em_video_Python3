from datetime import date
d = str(' Desafio 39 ')
print(f'\n{d:=^50}')

atual = date.today().year

nascimento = int(input('\nInforme o ano de seu nascimento: '))

print('\n[ 1 ] - Feminimo.')
print('[ 2 ] - Masculino.')

sexo = int(input('\nInforme seu sexo: '))

idade = atual - nascimento

print('\nQuem nasceu em {}. Tem {} anos, em {}.'.format(nascimento, idade, atual))
if sexo == 2:
    if idade == 18:
        print('Você tem que se alistar Imediatamente!!!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento!'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos!'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 1:
    print('Seu alistamento não é obrigatório!!!')
    print('Você não precisa se alistar, se não quiser.')
else:
    print('Opção do sexo inválida tente novamente!')