from datetime import date
print("=-" * 15)
print("   Classificando Atletas")
print("=-" * 15)
print("")

ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos.")
    print("A classificação desse atleta é MIRIM")
elif idade <= 14:
    print(f"O atleta tem {idade} anos.")
    print("A classificação desse atleta é INFANTIL")
elif idade <= 19:
    print(f"O atleta tem {idade} anos.")
    print("A classificação desse atleta é JUNIOR")
elif idade <= 20:
    print(f"O atleta tem {idade} anos.")
    print("A classificação desse atleta é SÊNIOR")
else:
    print(f"O atleta tem {idade} anos.")
    print("A classificação desse atleta é MASTER")