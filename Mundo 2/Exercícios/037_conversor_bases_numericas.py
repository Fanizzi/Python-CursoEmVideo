import math
print("=-" * 15)
print("    Conversor de Bases Numéricas")
print("=-" * 15)

n = int(input("Digite um número inteiro qualquer: "))

print("1 - para binário")
print("2 - octal")
print("3 - hexadecimal")
opcao = int(input("Escolha uma das opções acima: "))

if opcao == 1:
    print(f"A conversão de {n} para binário é: {bin(n)[2:]}")
elif opcao == 2:
    print(f"A conversão de {n} para octal é: {oct(n)[2:]}")
elif opcao == 3:
    print(f"A conversão de {n} para hexadecimal é: {hex(n)[2:]}")
else:
    print("Digite uma opção válida.")
