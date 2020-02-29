from Titulo import Titulo

d = Titulo(61, 'Progressão Aritmética!!!')
d.Desafio()

print('Gerador de PA.')
print('-=' * 10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = int(1)

while contador <= 10:
     print(f'{termo} ► ', end='')
     termo += razao
     contador += 1
print('Fim!')


