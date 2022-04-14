"""
    Para criarmos um laço de repetição utilizando o 'for', nós construímos a seguinte estrutura:

                                        range = Quantas vezes o laço irá se repetir
        for c in range(1, 10):          c = Variável 
            passo                       passo = Comando que está sendo executado dentro do laço
        pega                            pega = Comando que vai ser executado dps do laço terminar


        Exs:

            for c in range(0, 6):       Nesse laço, ele irá escrever 'oi' 6 vezes, pois ele está considerando
                print('oi')             o 0, porem ele desconsidera o ultimo algarismo, que é o 6.            
            print('FIM')                            
                                        

            for c in range(1, 6):      Nesse laço, ele irá escrever 'oi' 5 vezes, pois ele está começando
                print('oi')            a partir do 1, também desconsiderando o ultimo algarismo, que é o 6.
            print('FIM')               
                                       


            for c in range(6, 0, -1):   Nesse laço, ele irá escrever do número 6 ao 0, pois colocamos o -1
                print(c)                depois da segunda virgula. A função dela é fazer de trás para frente.
            print('FIM')                O resultado será: 6, 5, 4, 3, 2, 1, 0.


            for c in range(0, 7, 2):    Nesse laço, o programa irá escrever do número 0 até o 6 de 2 em 2.
                print(c)                O resultado será: 0, 2, 4 e 6
            print('Fim')


            n = int(input('Digite um número: '))     Nessa estrutura, nós estamos pegando o número digitado recebido
            for c in range(0, n+1)                   pela variável 'n' e colocando dentro do range do laço.
                print(c)                             o '+1' depois da variável 'n' serve para que o número digitado
            print('Fim')                             seja considerado no for. Pois o ultimo número do range
                                                     é sempre desconsiderado


            i =  int(input('Início: '))        Nessa estrutura, o laço irá pegar utilizar as variáveis 'i, f, p'                      
            f = int(input('Fim: '))            dentro do range. Essas variáveis possuem o valor digitado pelo
            p = int(input('Passo: '))          usuário.
            for c in range(i, f+1, p)
                print(c)                                         
            print('Fim') 
"""