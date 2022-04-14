real = float(input('Quanto dinheiro você possui na carteira? R$'))
conversao = real / 5.16  #Alterar esse valor de acordo com o valor do Dolar.
print(f'Com R${real} você pode comprar U${conversao:.2f}')