n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 0.5  # ou (1/2)

print('Número digitado: {} \n O dobro de {} é {}. \n O triplo de {} é {}. \n A raiz quadrada de {} é {:.2f}.' .format(n, n, d, n, t, n, r))


# UTILIZANDO APENAS 1 VARIAVEL
n1 = int(input('Digite um número: '))
print('Número digitado: {} \n O dobro de {} é {}. \n O triplo de {} é {}. \n A raiz quadrada de {} é {:.2f}.' .format(n1, n1, (n1 * 2), n1, (n1 * 3), n1, pow(n1, (1/2))))
