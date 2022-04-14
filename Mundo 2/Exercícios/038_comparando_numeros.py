print("=-" * 15)
print("    Comparando Números")
print("=-" * 15)
print("")

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(f"O primeiro valor é maior.")
elif n2 > n1:
    print(f"O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
