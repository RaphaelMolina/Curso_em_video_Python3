from Titulo import Titulo

e = Titulo(66, 'Somando os números!!!')
e.Exercicio()
soma = contador = numero = int()

while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'\nA soma dos {contador} valores foi {soma}!')