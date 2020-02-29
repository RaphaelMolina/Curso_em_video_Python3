from Titulo import Titulo

e = Titulo(62, 'Progressão Aritmética a escolha!!!')
e.Exercicio()

termo = int(input('Informe o primeiro termo da PA: '))
razão = int(input('Informe a razão da PA: '))
final = int((razão * 10) + termo)
contador = int(1)
mais = int(1)

print('\nAqui estão os 10 primeiros termos da PA:\n')
while termo < final:
    print(f'{contador}º Termo → {termo}.')
    termo += razão
    contador += 1
    if termo >= final:
        mais = int(input('\nGostaria de ver mais Termos, quantos? '))
        final += (razão * mais)
print('\nFim!')
