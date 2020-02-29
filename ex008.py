limpar = str('\033[m')

texto = {'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'verde2':'\033[36m'}

e = str('{} Exercício 8 {}'.format(texto['vermelho'], texto['verde2']))
print('{}{:=^30}{}\n'.format(texto['verde2'], e, limpar))

d = float(input('{}Informe uma distância em metros: {}'.format(texto['roxo'], limpar)))
km = float(d/1000) # 1 km - Kilometro = 1.000 metros
hm = float(d/100)  # 1 hm - Hectômetro = 100 metros
dam = float(d/10)  # 1 dam - Decâmetro = 10 metros
dm = float(d*10)   # 1 dm - Decímetro = 10 centimetros
cm = float(d*100)  # 1 cm - Centrimetro = 10 milímetros
mm = float(d*1000) # 1 mm - Milímetro = 1000 micrômetro

print('\nA medida de {}{}{} m corresponde a:\n{}{}{} km\n{}{}{} hm\n{}{}{} dam\n{}{:.0f}{} dm\n{}{:.0f}{} cm\n{}{:.0f}{} mm'
      .format(texto['vermelho'], d, limpar, texto['verde2'], km, limpar, texto['roxo'], hm, limpar, texto['vermelho'],
              dam, limpar, texto['verde2'], dm, limpar, texto['roxo'], cm, limpar, texto['vermelho'], mm, limpar))
