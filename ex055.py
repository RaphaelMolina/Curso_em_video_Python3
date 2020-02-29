from Titulo import Titulo

e = Titulo(55, 'Analisando o Maior e o Menor peso informado!!!')
e.Exercicio()
menor = float()
maior = float()

for contador in range(0, 5):
    p = float(input('Informe seu peso: '))
    if contador == 0:
        menor = p
        maior = p
    elif menor > p:
        menor = p
    elif maior < p:
        maior = p

print(f'\nO Maior peso informado foi {maior}. E o menor peso informado foi {menor}.')

