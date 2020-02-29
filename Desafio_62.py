from Titulo import Titulo

d = Titulo(62, 'Super Progressão Aritmética!!!')
d.Desafio()

print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = int()
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} ► ', end='')
        termo += razao
        contador += 1
    print('Pausa.')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('\nFim!\n')
print(f'Progressão finalizada com {total} termos apresentados.')
