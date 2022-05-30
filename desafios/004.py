# CÁLCULO PARA PINTURA DE PAREDE
# CADA LITRO DE TINTA PINTA 2M²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede de {} por {}, tem área de {}m2.'.format(larg, alt, area))
print('Para pintar essa parede, serão necessários {}lts de tinta.'.format(tinta))
