l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

area = l * a
litros = area / 2  #Quantidade de metros que 1 litro de tinta pinta
print(f'Sua parede possuí as dimensões {l}x{a} e sua área é de {area}m². \nPara pintar essa parede, você precisará de {litros}L de tinta.')
