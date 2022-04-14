#### Análise

    # len(frase)       - Serve para ver o comprimento da string (ver a quantia de caracteres)
    # frase.count('o') - É usado para contar quantas vezes existe a letra que está dentro das aspas dentro da string 
    # frase.find('deo')- Ele irá dizer quantas vezes ele encontrou a combinação de letras que está nas aspas dentro da string
    #                    Quando o python não encontrar a frase dentro das aspas, significa que aquilo escrito não existe na string.
    # 'Curso' in frase - Ele irá responder True ou False se terá aquilo que está escrito dentro das aspas na string.

#### Transformação

    # frase.replace('Python', 'Android') - O Python será substituido pela frase 'Android' na string dentro da variavel 'frase'
    # frase.upper() - Transformará todas as letras da string em MAIÚSCULAS
    # frase.lower() - Transformará todas as letras da string em MINÚSCULAS
    # frase.capitalize() - Transformará todas as letras da string em minúsculas, deixando apenas a primeira letra em Maiúscula
    # frase.title() - Irá transformar todas as primeiras letras depois de espaços em Maiúsculas
    # frase.strip()    - Remove todos os espaços do inicio e do fim da string
        # frase.rstrip()  - Remove somente os espaços da direita no final string
        # frase.lstrip()  - Remove somente os espaços da esquerda do inicio da string

#### Divisão

    # frase.split() - o Split irá tirar todos os espaços entre as frases da string, e cada palavra recebera uma nova indexação nova
    #                 Ou seja, cada palavra que era separada por um espaço, será transformada em uma nova lista

#### Junção

    # '-'.join(frase) - Ele irá juntar todos os elementos de frase, usando o traço dentro das aspas
    #                   É possivel deixar uma espaço ali dentro para ter espaços entre os elementos tambem.
    # print("""""") - Utilizando 3 aspas duplas no print, eu posso colocar textos grandes sem precisar colocar
    #                 vários prints ou \n para pular para linhas de baixo.