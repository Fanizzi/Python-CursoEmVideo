from math import hypot
catetoOposto = int(input('Digite o valor do cateto oposto: '))
catetoAdjascente = int(input('Digite o valor do cateto adjascente: '))

hip = hypot(catetoOposto, catetoAdjascente)
print(f'O comprimento da hipotenusa é de: {hip:.2f}')
