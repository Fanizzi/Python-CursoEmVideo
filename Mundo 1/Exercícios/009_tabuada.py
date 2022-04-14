n1 = int(input('Digite um número para ver sua tabuada: '))

res1 = n1 * 1
res2 = n1 * 2
res3 = n1 * 3
res4 = n1 * 4
res5 = n1 * 5
res6 = n1 * 5
res7 = n1 * 7
res8 = n1 * 8
res9 = n1 * 9
res10 = n1 * 10

print('=================')
print(f'{n1} x 1 = {res1}')
print(f'{n1} x 2 = {res2}')
print(f'{n1} x 3 = {res3}')
print(f'{n1} x 4 = {res4}')
print(f'{n1} x 5 = {res5}')
print(f'{n1} x 6 = {res6}')
print(f'{n1} x 7 = {res7}')
print(f'{n1} x 8 = {res8}')
print(f'{n1} x 9 = {res9}')
print(f'{n1} x 10 = {res10}')
print('=================')



# Método utilizando for e range muito mais facil
n2 = int(input("Digite um número para ver sua tabuada: "))
print('=================')
for i in range(1, 10+1):
    print(f"{n2} x {i} = {n2 * i}")

print('=================')