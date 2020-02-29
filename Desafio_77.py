from Titulo import Titulo

d = Titulo(77, 'Contando vogais em Tupla!!!')
d.Desafio()

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
