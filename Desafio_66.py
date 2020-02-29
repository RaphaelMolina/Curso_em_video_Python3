from Titulo import Titulo

d = Titulo(66, 'Vários números com flag!!!')
d.Desafio()
quantidade = soma = int()
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print(f'A soma dos {quantidade} valores foi {soma}!')
print('Fim!')
