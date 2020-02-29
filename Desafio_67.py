from Titulo import Titulo

d = Titulo(67, 'Tabuada!!!')
d.Desafio()

while True:
    numero = int(input('Quer ver a Tabuada de qual valor? '))
    print('-' * 30)
    if numero < 0:
        break
    for contador in range(1, 11):
        print(f'{numero} X {contador} = {numero * contador}')
    print('-' * 30)
print('Programa Tabuada encerrado. Volte sempre!')
