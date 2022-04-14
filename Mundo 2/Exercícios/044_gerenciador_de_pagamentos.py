print("=-" * 15)
print("    Gerenciador de Pagamentos")
print("=-" * 15)
print("")

p_valor = float(input("Informe do valor do produto: "))
print("")
print("1 - Dinheiro/Cheque (10% de Desconto)")
print("2 - A Vista no Cartão (5% de Desconto)")
print("3 - Em até 2x no Cartão")
print("4 - 3x ou mais no Cartão (20% de Juros)")
print("")
opcao = int(input("Escolha umas das formas de pagamento acima: "))
print("=-" * 15)

if opcao == 1:
   v_total = p_valor - (p_valor * 0.10)
   print(f"O produto custará {v_total}"
         "\nMétodo de Pagamento: Dinheiro/Cheque (10% de Desconto)")
   print("=-" * 15)

elif opcao == 2:
    v_total = p_valor - (p_valor *0.05)
    print(f"O produto custará {v_total}"
         "\nMétodo de Pagamento: A Vista no Cartão (5% de Desconto)")
    print("=-" * 15)

elif opcao == 3:
    print(f"O produto custará {p_valor}"
         "\nMétodo de Pagamento: Em até 2x no Cartão (Preço Normal)")
    print("=-" * 15)

else:
    v_total = p_valor + (p_valor * 0.20)
    print(f"O produto custará {v_total}"
         "\nMétodo de Pagamento: 3x ou mais no Cartão (20% de Juros)")
    print("=-" * 15)