#A biblioteca 'math' é uma biblioteca de matemática que adiciona
# mais alguns elementos da matematica além das quais nós já utilizamos dentro do python
# Dentro da biblioteca 'math' nós temos:
#  - ceil       - Arredondamento de um numero para cima
#  - floor      - Arredondamento de um numero para baixo
#  - trunc      - Vai eliminar todos os números depois da virgula
#  - pow        - Potencia
#  - sqrt       - Calcular raiz quadrada
#  - factorial  - Calcular o fatorial de um número
# Fora essas funcionalidades, temos muitas outras dentro da biblioteca math...

# para importar uma biblioteca, nós precisamos utilziar o 'import' e depois o nome da biblioteca.
# Exemplo --  import math
# Se utilizar import math, ele irá importar todas as funcionalidades listadas a cima.
# Agora para importar uma funcionalidade específica, utilize: from math import sqrt. 
# Com esse comando a cima irá importar a funcionalidade da raiz quadrada, sem importar outras.

#Caso queira importar mais de uma, utilize:
# from math import sqrt, pow
# utilize a virgula para colocar outra funcionalidade que você deseja no import.

# Exemplo:

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}.')

# Exemplo 2

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)  # Ao fazer a importação da funcionalidade especifica da raiz quadrada, nós não precisamos
                  # de colocar o math. e a funcionalidade. Nós já colocamos o nome da funcionalidade direto.
print(f'A raiz de {num} é igual a {raiz:.2f}.')

