d = int(input('Digite a distancia em Km da sua viagem: '))
if d <= 200:
    preco = d * 0.50
    print(f'A sua viagem de {d}Km custará R${preco}.')
else:
    preco = d * 0.45
    print(f'A sua viagem de {d}Km por ser mais longa, custará R${preco}')