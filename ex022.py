e = str(' Exercício 22 ')
print('{:=^30}\n'.format(e))

nome_completo = str(input('Digite seu nome Completo: ')).strip()# Irá elinimar os espaços no inicio e no final do nome digitado.
print('\nAnalisando seu nome...\n')
print('Seu nome em maiúsculas é {}'.format(nome_completo.upper()))
print('Seu nome em minúsculas é {}'.format(nome_completo.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome_completo.replace(' ', ''))))
print('Seu nome tem ao todo {} letras'.format(len(nome_completo) - nome_completo.count(' ')))
print('Seu primeiro nome é {}, e tem {} letras'.format(nome_completo.split()[0], nome_completo.find(' ')))
print('Seu primeiro nome é {}, e tem {} letras'.format(nome_completo.split()[0], len(nome_completo.split()[0])))
