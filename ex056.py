from Titulo import Titulo

e = Titulo(56, 'Análise de idade!!!')
e.Exercicio()
m = int()
v = str()
maior = int()
menor = int()
for contador in range(0, 4):
    n = str(input('\nInforme seu nome: '))
    i = int(input('Informe a sua idade: '))
    m += i
    s = str(input('Informe seu sexo (F para Feminimo e M para Masculino): ')).upper()[0]
    if s == 'M' and maior < i:
        maior = i
        v = n
    elif s == 'F' and i < 20:
        menor += 1

print(f'\nA média de todas as idades informadas é de {m//4} anos.')
if v == '':
    print('Nenhum Homen foi informado.')
else:
    print(f'O Homen mais velho é o {v}.')
if menor == 0:
    print('E nenhuma Mulher tem menos de 20 anos, ou nenhuma Mulher foi informada.')
elif menor == 1:
    print('E apenas uma mulher tem menos de 20 anos.')
else:
    print(f'E {menor} Mulheres tem menos de 20 anos.')

