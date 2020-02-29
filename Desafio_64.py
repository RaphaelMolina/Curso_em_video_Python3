from Titulo import Titulo

d = Titulo(64, 'Tratando vários valores!!!')
d.Desafio()

soma = contador = int()

numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'\nVocê digitou {contador} números e a soma entre eles foi {soma}.')
