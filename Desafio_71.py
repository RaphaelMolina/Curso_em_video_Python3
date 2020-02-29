from Titulo import Titulo

d = Titulo(71, 'Simulador de Caixa Eletrônico!!!')
d.Desafio()
print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))
cedula = int(50)
total_cedula = int()

while True:
    if valor >= cedula:
        valor -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula:.2f}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if valor == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
