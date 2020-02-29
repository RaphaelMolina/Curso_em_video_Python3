import pygame
e = str(' Exercício 21 ')
print('{:=^30}\n'.format(e))
pygame.mixer.init()
pygame.mixer.music.load('black.mp3')
pygame.mixer.music.play()
input('Precione qualquer tecla para parar a execução: ')

