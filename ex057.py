from Titulo import Titulo

e = Titulo(57, 'Leitura de sexo!!!')
e.Exercicio()

r = str()
s = str()

while r != 's':
    s = str(input('Informe o sexo [M / F]: '))
    if s == 'M':
        r = 's'
    elif s == 'm':
        r = 's'
    elif s == 'F':
        r = 's'
    elif s == 'f':
        r = 's'
    else:
        print('\nO valor digitado é invalido!')
print('\nObrigado, Fim!')
