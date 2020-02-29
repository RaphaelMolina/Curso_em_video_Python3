from Titulo import Titulo

d = Titulo(69, 'Análise de dados do grupo!!!')
d.Desafio()

mulher = homem = maior = int()

while True:
    idade = int(input('Idade: '))
    sexo = str(' ')
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resposta = str(' ')
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('\nFim!')
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} Homens cadastrados.')
print(f'E temos {mulher} Mulheres com menos de 20 anos.')
