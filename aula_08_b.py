import random
import emoji
print(emoji.emojize('Olá, Mundo! :smile:', use_aliases=True))

numero = random.random() # O método random da classe random gera um número real de 0 a 1
numero2 = random.randint(1, 10) # O método randint da classse random gera um número inteiro de tal número a tal número seguindo os parâmetros informados.
print(numero)
print(numero2)
