def tinta (larg,alt):
    area = larg * alt
    tinta = area / 2
    print('Sua parede tem dimensão de {} x {} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta'.format(larg, alt, area, tinta))

larg = float(input('Qual a largura da sua parede?: '))
alt = float(input('Qual a altura da sua parede?: '))
tinta(larg, alt)