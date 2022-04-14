dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KMs o carro andou? '))
valor_final = dias * 60 + km * 0.15

print(f'O preço a pagar pelo veículo alugado será de {valor_final}')