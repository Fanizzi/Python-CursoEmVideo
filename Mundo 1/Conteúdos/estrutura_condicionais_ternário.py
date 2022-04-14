"""
Estruturas condicionais
if (se)
else (senao)
"""
idade = 10
condicao = idade >= 18
if idade <=13:
    print("Criança")
elif idade <= 18:
    print("Adolescente")
else:
    print("Adulto")

"""
Operadores ternário
""" 

idade = 16
#resultado = ('Menor idade', 'Maior idade')[idade>=18]
resultado = 'Maior idade' if idade>=18 else 'Menor idade'
print(resultado)