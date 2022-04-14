n = str(input("Digite seu nome: ")).strip()
nome = n.split()
print(f"Primeiro nome: {nome[0]}")
print(f'Ultimo nome: {nome[len(nome)-1]}')