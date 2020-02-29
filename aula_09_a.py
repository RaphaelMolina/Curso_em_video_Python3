aula_09 = str(' Aula 09 ')
aula_09 = str(' Aula 09 ')
print('{:=^30}\n'.format(aula_09))
#Fatiamento da cadeia de caracteress
frase = str('Curso em Vídeo Python')
frase2 = str('   Aprenda Python  ')
frase3 = ['Curso', 'em', 'Vídeo', 'Python']
print(frase[9])
# Exibe apenas o índice selecionado(Caracter selecionado)
print(frase[9:13])
# Exibe o intervalo de caracteres selecionados incluindo o primeiro e não incluindo o último
print(frase[9:14])
# Exibe o intervalo de caracteres selecionados incluindo o primeiro e não incluindo o último
print(frase[9:21])
# Exibe o intervalo de caracteres selecionados incluindo o primeiro e não incluindo o último
print(frase[9:21:2])
# Exibe o intervalo de caracteres selecionados, pulando com um intervalo de 2 em 2, incluindo o primeiro e não incluindo o último
print(frase[:5])
# Quando o inicio não é informado ele irá exibir dês do inicio do conjunto de caracteres
print(frase[15:])
# Quando o final não é informado ele irá exibir até o final do conjunto de caracteres
print(frase[9::3])
# Quando o final não é informado ele irá exibir até o final do conjunto de caracteres, e neste caso pulando de 3 em 3

# Análise de Caracteres

print(len(frase)) # Comprimento
# Informa o número de caracteres que compõe o conjunto de caracteres selecionado
print(frase.count('o')) # Contagem
# Conta a quantidade de vezes que o parâmetro informado se repete
print(frase.count('o', 0, 13)) # Contagem
# Conta a quantidade de vezes que o parâmetro informado se repete, considerando o intervalo solicitado
print(frase.find('deo')) # Encontrar
# Irá encontrar em qual posição se inicia o parâmetro informado
print(frase.find('Android'))
# Quando não houver o parâmetro informado no conjunto de caracteres que esta sendo analisado, terá um retorno = -1
print('Curso' in frase) # Operador
# Verifica se existe a string informada dentro da vareavel informada

# Transformação

print(frase.replace('Python', 'Android'))# Trocar
# Substitui a string informada por outra string informada
print(frase.replace('o', 'a'))
# Substitui a string informada por outra string informada
print(frase.replace(' ', ''))
print(frase.upper())
# Altera todos os caracteres minúsculos para maiúsculos
print(frase.lower())
# Altera todos os caracteres maiúsculos para minúsculos
print(frase.capitalize())
# Capitaliza toda a string, deixa apenas a primeira letra da string maiúscula
print(frase.title())
# Irá deixar maiúscula a primeira letra de cada palavra da string
print(frase2)
print(frase2.strip())
# Remove os espaços do começo e do final da String
print(frase2.rstrip())
# Remove os espaços do direita da string(Final)
print(frase2.lstrip())
# Remove os espaços da esquerda da string(começo)

# Divisão

print(frase.split())
# Cria uma lista com todas as palavras dentro da vareavel, divide, separa as palavras

# Junção

print('-'.join(frase3))
# Junta varias strings de uma lista, com o separador informado como parâmetro
print(' '.join(frase3))
print('_'.join(frase))
# Se não estiver separado ou em lista, irá colocar o separador entra cada caracter

