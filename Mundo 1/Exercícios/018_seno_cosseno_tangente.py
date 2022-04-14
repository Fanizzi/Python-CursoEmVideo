from math import cos, sin, tan, radians
angulo = int(input('Digite o valor do angulo: '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tg = tan(radians(angulo))

print(f'O angulo {angulo} tem os valores do cosseno {cosseno}, seno {seno}, tangente {tg}.')
