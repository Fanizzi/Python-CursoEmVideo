s = 0
n = int(input('Informe o número: '))
for c in range(1, n+1):
    if n % c == 0:
        s += 1
if s > 2:      
    print('O número não é primo.')
else:
    print('O número é primo.')