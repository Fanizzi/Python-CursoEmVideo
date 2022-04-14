from datetime import date
print("=-" * 15)
print("    Alistamento Militar")
print("=-" * 15)
print("")

ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
ano_alistamento = ano_atual - ano_nascimento
tempo_q_falta = 18 - ano_alistamento
tempo_q_passou = ano_alistamento - 18

print("")
if ano_alistamento < 18:
    print("Ainda vai se alistar ao serviço militar.")
    print(f"Faltam ainda {tempo_q_falta} anos.")
elif ano_alistamento == 18:
    print("Já está na hora de se alistar ao serviço militar.")
else:
    print("Já passou do tempo de alistamento...")
    print(f"Passaram-se {tempo_q_passou} ano(s) do prazo de alistamento.")
