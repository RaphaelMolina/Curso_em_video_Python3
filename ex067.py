from Titulo import Titulo

e = Titulo(67, 'Tabuada!!!')
e.Exercicio()

numero = resultado = contador = int()
while True:
    numero = int(input('Quer ver a Tabuada de qual valor? '))
    if numero < 0:
        print('\nPrograma Tabuada encerrado. Volte sempre!')
        break
    else:
        print('=' * 15)
        while contador < 10:
            contador += 1
            resultado = numero * contador
            print(f'{numero} X {contador} = {resultado}')

        print('=' * 15)
        contador = 0

