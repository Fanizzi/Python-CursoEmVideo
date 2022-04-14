s = float(input('Digite o salário do funcionário: '))
if s <= 1250:
    aumento = s * 0.15
    salario_novo = s + aumento  
    print(f'O salario do funcionário com aumento, será {salario_novo}')
else:
    aumento = s * 0.10
    salario_novo = s + aumento
    print(f'O novo salário do funcionário será {salario_novo}')