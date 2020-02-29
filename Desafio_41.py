from datetime import date

d = str(' Desafio 41 ')
print(f'\n{d:=^50}')

atual = date.today().year
nascimento = int(input('\nAno de nascimento: '))
idade = atual - nascimento

print('\nO atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: Mirin.')
elif idade <= 14:
    print('Classificação: Infantil.')
elif idade <= 19:
    print('Classificação: Junior.')
elif idade <= 25:
    print('Classificação: Sênior.')
else:
    print('Classificação: Master')