from Titulo import Titulo

d = Titulo(56, 'Analisador completo!!!')
d.Desafio()

media = int()
nomeh = str()
maior = int()
total = int()
soma = int()
for contador in range(1, 5):
    print('\n----- {}ª Pessoa -----'.format(contador))
    nome = (input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip()
    soma += idade
    if contador == 1 and sexo in 'Mm':
        maior = idade
        nomeh = nome
    if sexo in 'Mn' and idade > maior:
        maior = idade
        nomeh = nome
    if sexo in 'Ff' and idade < 20:
        total += 1
media = soma / 4
print('\nA média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomeh))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(total))

