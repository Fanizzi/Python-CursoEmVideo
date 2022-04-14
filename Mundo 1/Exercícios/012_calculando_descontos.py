preco = float(input('Qual é o preço do produto? R$'))
desconto = preco * 0.05
precoatual = preco - desconto
print(f'O produto que custava {preco}, na promoção com desconto de 5% vai custar {precoatual:.2f}')
