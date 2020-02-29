from Titulo import Titulo

e = Titulo(77, 'Vogais das Palavras!!!')
e.Exercicio()
tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro', 'felicidade', 'liberdade', 'financeira')

vogais = ('A', 'E', 'I', 'O', 'U')

contador = int()
tamanho = len(tupla)

while contador < tamanho:
    palavra = len(tupla[contador])
    inicio = 0
    print(f'Na palavra {tupla[contador].upper(): <11} temos as vogais: ', end='')
    while inicio < palavra:
        if tupla[contador][inicio].upper() in vogais:
            print(tupla[contador][inicio], end=' ')
        inicio += 1
    contador += 1
    print('')
