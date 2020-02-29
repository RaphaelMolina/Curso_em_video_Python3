e = str(' Exercício 14 ')
print('{:=^30}\n'.format(e))
temperatura_celsius = float(input('Informe a temperatura em ºC: '))
temperatura_fahrenheit = float(32 + (temperatura_celsius * 9 / 5))
temperatura_fahrenheit2 = float(((9 * temperatura_celsius) / 5) + 32)
temperatura_fahrenheit3 = float(9 * temperatura_celsius / 5 + 32)

print('\nA temperatura de {}ºC corresponde a {}ºF!'.format(temperatura_celsius, temperatura_fahrenheit))
print('\n', temperatura_fahrenheit2, '\n', temperatura_fahrenheit3)
