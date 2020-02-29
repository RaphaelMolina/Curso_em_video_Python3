from Titulo import Titulo

e = Titulo(71, 'Caixa Eletrônico!!!')
e.Exercicio()

print('=' * 30)
print(' ' * 5, 'Banco Curso em Vídeo', ' ' * 5)
print('=' * 30)

valor = int(input('Que valor você quer sacar? '))
cinquenta = vinte = dez = um = int()
while True:
    if valor >= 50:
        cinquenta += 1
        valor -= 50
    elif 50 > valor >= 20:
        vinte += 1
        valor -= 20
    elif 20 > valor >= 10:
        dez += 1
        valor -= 10
    elif 10 > valor >= 1:
        um += 1
        valor -= 1
    elif valor == 0:
        if cinquenta == 1:
            print('Total de uma cédula de R$ 50,00.')
        elif cinquenta > 1:
            print(f'Total de {cinquenta} cédulas de R$ 50,00.')
        if vinte == 1:
            print('Total de uma cédula de R$ 20,00.')
        elif vinte > 1:
            print(f'Total de {vinte} cédulas de R$ 20,00.')
        if dez == 1:
            print('Total de uma cédula de R$ 10,00.')
        elif dez > 1:
            print(f'Total de {dez} cédulas de R$ 10,00.')
        if um == 1:
            print('Total de uma cédula de R$ 1,00.')
        elif um > 1:
            print(f'Total de {um} cédulas de R$ 1,00.')
        print('=' * 30)
        print('Volte sempre ao Banco Curso em Vídeo! Tenha um Bom dia!')
        break
