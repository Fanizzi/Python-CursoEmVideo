from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
n_aleatorio = randint(0, 5)  #Faz o computador gerar um número entre 0 e 5
res = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if res == n_aleatorio:
    print('Parabéns, você acertou o número que o computador pensou!')
else:
    print('Infelizmente você não acertou o número :(')