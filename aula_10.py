# tempo = int(input('Quantos anos tem seu carro?\n'))
# if tempo <=3:
    # print('Carro Novo!')
# else:
    # print('Carro Velho!')
# print('\n--- Fim! ---')

# Ou

# tempo2 = int(input('\nQuantos anos tem seu carro?\n'))
# print('Carro Novo!' if tempo<=3 else 'Carro Velho!')
# print('\n--- Fim! ---')

nome = str(input('Qual é o seu nome?\n'))
if nome == 'Raphael':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('É um prazer te conhecer {}!'.format(nome))

nota1 = float(input('\nDigite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) /2
print('\nA sua média é {:.1f}'.format(media))
if media >= 6.0:
    print('Sua média foi boa, Parabéns!')
else:
    print('Sua média foi ruim, Estude mais!')
print('\nSua média foi boa, Parabéns!' if media >=6.0 else '\nSua média foi ruim, Estude mais!')
