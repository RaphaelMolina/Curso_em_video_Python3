d = str(' Desafio 43 ')
print(f'\n{d:=^50}')

peso = float(input('\nQual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)

print('\nO seu IMC é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você esta abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('Parabéns, você esta na faixa de peso normal!')
elif 25 <= imc < 30:
    print('Você esta em sobrepeso!')
elif 30 <= imc < 40:
    print('Você esta em Obesidade, cuidado!!')
elif imc >= 40:
    print('Você esta em Obesidade Mórbida, procure ajuda!!!')

