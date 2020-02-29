e = str('Exercício 43')
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n\033[4;32mCalculando o IMC (Índice de Massa Corporal)!!!\033[m')

print('\nInformações do sistema:')
print('IMC até 18.4: \033[31mAbaixo do peso\033[m!')
print('IMC de 18.5 até 25: \033[32mPeso ideal\033[m!')
print('IMC de 25.1 até 30: \033[33mSobrepeso\033[m!')
print('IMC de 30.1 até 40: \033[34mObesidade\033[m!')
print('IMC de 40.1 em diante: \033[35mObesidade mórbida\033[m!')

altura = float(input('\nInforme a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = float(peso / (altura * altura))

if imc <= 18.4:
    print('\nSeu IMC é de \033[36m{:.1f}\033[m.'.format(imc))
    print('Você esta \033[31mAbaixo do peso\033[m!')
elif imc >= 18.5 and imc <= 25:
    print('\nSeu IMC é de \033[36m{:.1f}\033[m.'.format(imc))
    print('Você esta no \033[32mPeso ideal\033[m!')
elif imc >= 25.1 and imc <= 30:
    print('\nSeu IMC é de \033[36m{:.1f}\033[m.'.format(imc))
    print('Você esta com \033[33mSobrepeso\033[m!')
elif imc >= 30.1 and imc <= 40:
    print('\nSeu IMC é de \033[36m{:.1f}\033[m.'.format(imc))
    print('Você esta com \033[34mObesidade\033[m!')
elif imc > 40:
    print('\nSeu IMC é de \033[36m{:.1f}\033[m.'.format(imc))
    print('Você esta com \033[35mObesidade mórbida\033[m!')



