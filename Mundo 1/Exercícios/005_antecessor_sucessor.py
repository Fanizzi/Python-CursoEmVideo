n1 = int(input('Digite um número: '))
a = n1 - 1
s = n1 + 1
print('Analisando o número {}, o seu antecessor é {}, e o seu sucessor é {}' .format(n1, a, s))


# UTILIZANDO APENAS 1 VARIAVEL

n = int(input('Digite um número: '))
print('Analisando o número {}, o seu antecessor é {}, e o seu sucessor é {}' .format(n, (n-1), (n+1)))