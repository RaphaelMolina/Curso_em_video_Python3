from Titulo import Titulo

e = Titulo(69, 'Cadastro de Pessoas!!!')
e.Exercicio()

print('=' * 7, 'Fim do Programa', '=' * 7)

mulher = homem = maior = int()

while True:
    print('-' * 30)
    print('Cadastre uma Pessoa.')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        print('=' * 7, 'Fim do Programa', '=' * 7)
        print(f'Total de pessoas com mais de 18 anos é igual a {maior}.')
        if homem == 0:
            print('Não tivemos Homens cadastrados.')
        elif homem == 1:
            print('Ao todo tivemos um Homem cadastrado.')
        else:
            print(f'Ao todo temos {homem} Homens cadastrados.')
        if mulher == 0:
            print('Não tivemos Mulheres com menos de 20 anos cadastradas.')
        elif mulher == 1:
            print('E tivemos uma Mulher com menos de 20 anos cadastrada.')
        else:
            print(f'E tivemos {mulher} com menos de 20 anos cadastradas.')
        break
