print("=-"*15)
print("     Empréstimo Bancário")
print("=-"*15)
print("")
valor_casa = float(input("Qual o valor da casa á ser comprada? "))
salario_comprador = float(input("Informe o salário do comprador: R$ "))
anos = int(input("Quantos anos o comprador pretende pagar a casa? "))
meses = anos * 12

prestacao_mensal = valor_casa / meses

if prestacao_mensal < 0.3 * salario_comprador:
    print("O empréstimo foi APROVADO!")
    print(f"O comprador terá que pagar R$ {prestacao_mensal:.2f} por mês, durante {anos} anos.")
elif prestacao_mensal > 0.3 * salario_comprador:
    print(f"Para pagar uma casa de R${valor_casa} em {anos} anos, a prestação será de R${prestacao_mensal:.2f} por mês")
    print("O empréstimo foi NEGADO!")
    print("A prestação mensal excedeu 30% do salário do comprador.")
