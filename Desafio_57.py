from Titulo import Titulo

d = Titulo(57, 'Validação de dados!!!')
d.Desafio()

sexo = str(input('Informe seu sexo [M / F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
