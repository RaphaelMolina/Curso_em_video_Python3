e = str('Exercício 42')
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n\033[4;32mVerificando o triângulo criado!!!\033[m')

lado1 = float(input('\nInforme o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))

print('\nInformações do sistema:')
print('O sistema irá verificar se é possivél formar um triângulo com os lados informados.')
print('Se todos os lados forem iguas, será um triângulo \033[31mEquilátero\033[m.')
print('Se dois lados forem iguas, será um triângulo \033[36mIsósceles\033[m.')
print('Se todos os lados forem diferentes, será um triângulo \033[32mEscaleno\033[m.')

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('\nO triângulo formado é \033[31mEquilátero\033[m!')
    elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2:
        print('\nO triângulo formado é \033[36mIsósceles\033[m!')
    elif lado2 == lado1 and lado2 != lado3 or lado2 == lado3 and lado2 != lado1:
        print('\nO triângulo formado é \033[36mIsósceles\033[m!')
    elif lado3 == lado1 and lado3 != lado2 or lado3 == lado2 and lado3 != lado1:
        print('\nO triângulo formado é \033[36mIsósceles\033[m!')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('\nO triângulo formado é \033[32mEscaleno\033[m!')
else:
    print('\n\033[1;31mOs lados informados não podem formar um triângulo!!!\033[m')
