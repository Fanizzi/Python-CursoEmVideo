'''
    Quando vamos iniciar uma estrutura de repetição, nós utilizamos o IF e o Else.
    Agora, nós podemos utilizar outra condição depois do if e antes do else, chamada de
    elif.
        Exemplo:
                if carro.esquerda():

                elif carro.direita():

                else:
    
    Nós podemos utilizar o 'elif' quantas vezes precisarmos.
    Porém nós não podemos utilizar o 'elif' sem utilizar o 'if' antes.

    Exemplo na prática:
'''

nome = str(input('Digite o seu nome: '))
if nome == 'Lorenzo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Gabriel':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia!')    