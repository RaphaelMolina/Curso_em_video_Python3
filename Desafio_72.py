from Titulo import Titulo

d = Titulo(72, 'Número por Extenso!!!')
d.Desafio()

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'catorze', 'qquize', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')

# Sem o quer continuar:
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'\nVocê digitou o número {contagem[numero]}.\n')

# Com o quer continuar:
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'\nVocê digitou o número {contagem[numero]}.\n')
        resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        while resposta not in 'SN':
            resposta = str(input('Desculpe não entendi. Você quer continuar? [S/N] ')).strip().upper()[0]
        if resposta == 'N':
            break
    else:
        print('Tente novamente. ', end='')
print('\nFim do Programa!')


