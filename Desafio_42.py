d = str(' Desafio 42 ')
print(f'\n{d:=^50}')

reta1 = float(input('\nPrimeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\nOs segmentos acima podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('Equilátero!!!')
    elif reta1 != reta2 != reta3 != reta1:
        print('Escaleno!!!')
    else:
        print('Isósceles!!!')
else:
    print('\nOs segmentos acima não podem formar um triângulo!')
