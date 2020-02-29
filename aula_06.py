# Deste modo o valor recebido será uma String.
numero = input('Digite um número: ')
print(numero)
print(type(numero)) # Informa o tipo do dado.
# Deste modo o valor recebido será uma String.
numero = str(input('Digite um número: '))
print(numero)
print(type(numero)) # Informa o tipo do dado.
# Deste modo o valor recebido será inteiro.
numero = int(input('Digite um número: '))
print(numero)
print(type(numero)) # Informa o tipo do dado.
# Deste modo o valor recebido terá um ponto flutuante.
numero = float(input('Digite um número: '))
print(numero)
print(type(numero)) # Informa o tipo do dado.
# Deste modo o valor recebido será um valor Booleano (True or False) - (Verdadeiro ou Falso).
numero = bool(input('Digite um número: '))
print(numero)
print(type(numero)) # Informa o tipo do dado.

numero = input('Digite um valor: ')
print(numero.isnumeric()) # Verifica se o valor recebido é númerico.
print(numero.isalpha()) # Verifica se o valor recebido é alfabetico.
print(numero.isalnum()) # Verifica se o valor recebido é alfanumerico.
print(numero.isupper()) # Verifica se o valor recebido esta maiusculo.
print(numero.islower()) # Verifica se o valor recebido esta minusculo.
print(numero.isprintable()) # Verifica se o valor recebido pode ser impresso.
print(numero.isspace()) # Verifica se o valor recebido é um espaço.

print(type(numero)) # Informa o tipo do dado.