v = int(input('Qual a velocidade que o carro está andando: '))
limite = 80
if v > limite:
    print('Você excedeu o limite de velocidade de 80km!')
    print('Você receberá uma multa de 7 reais por cada Km excedido!')
    v_excedida = v - limite
    multa = v_excedida * 7
    print(f'Você excedeu {v_excedida}km, você pagará R${multa} de multa!')
else:
    print('Parabéns! Você não excedeu o limite de velocidade de 80Km')
    
