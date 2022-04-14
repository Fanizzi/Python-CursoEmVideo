t = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
for c in range(1, 11):
    pa = t + (c-1)*r
    print(pa, end = ' -> ')
print('Fim')