from random import shuffle
nomes = []
for i in range(0,4):
    nomes.append(str(input(f'{i+1}º Aluno: ')))
shuffle(nomes)
print(nomes)