salario = float(input('Qual o salário do funcionário? R$'))
reajuste = salario * 0.15  # Outro método seria removendo a variavel "salario_final" 
                           # e transformando o deixando a variavel "reajuste" da seguinte forma:
                           # reajuste = salario + (salario * 15 / 100)
salario_final = salario + reajuste
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario_final:.2f}')