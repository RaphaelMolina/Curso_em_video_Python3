e = str(' Exercício 11 ')
print('{:=^30}\n'.format(e))

largura = float(input('Informe a largura de sua parede: '))
altura = float(input('Informe a altura de sua parede: '))
area = float(largura*altura)
tinta = float(area/2)
print('\nSua parede tem uma dimensão de {:.2f} X {:.2f} e uma área de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, voçê precisará de {:.2f}Lt de tinta.'.format(tinta))

