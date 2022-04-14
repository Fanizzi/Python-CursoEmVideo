n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'Sua média foi {m:.1f}')
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')

# Quando nós apenas utilizamos o if (sem o else), a estrutura de condição é chamada de simples.
# Agora quando usamos o else depois do if, a estrutura de condição é chamada de composta.
# Também é possivel utilizar o if e else juntos na mesma linha de código, porém só usamos
# quando a estrutura de condição é muito pequena e simples, por exemplo:
# print('PARABÉNS' if m >= 6 else 'Estude mais!')