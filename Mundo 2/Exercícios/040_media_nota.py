print("=-" * 15)
print("   Média de Nota")
print("=-" * 15)
print("")

n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))
m = (n1 + n2) / 2

if m < 5.0:
    print(f"REPROVADO! Sua média foi {m}")
elif m > 5.0 and m < 6.9:
    print(f"RECUPERAÇÃO! Sua média foi {m}")
else:
    print(f"APROVADO! Sua média foi {m}")