import random

print("=-"*15)
print("\033[31mMinigame de Jokenpô em Python!!\033[0m")
print("=-"*15)
print('')

print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jokenpo = ["Pedra", "Papel", "Tesoura"]

opcao = int(input('Oque você escolhe? '))
opcao_maquina = random.choice(jokenpo)

if opcao == 1 and opcao_maquina == 'Papel' or opcao == 2 and opcao_maquina == 'Tesoura' or opcao == 3 and opcao_maquina == 'Pedra':
    print(f"A Opção do jogador foi: {opcao}"
          f"\nA Opção da máquina foi: {opcao_maquina}"
          f"\nA máquina venceu!")

elif opcao == 1 and opcao_maquina == 'Tesoura' or opcao == 2 and opcao_maquina == 'Pedra' or opcao == 3 and opcao_maquina == 'Papel':
    print(f"A Opção do jogador foi: {opcao}"
          f"\nA Opção da máquina foi: {opcao_maquina}"
          f"\nO jogador venceu!")

else:
    print(f"A Opção do jogador foi: {opcao}"
          f"\nA Opção da máquina foi: {opcao_maquina}"
          f"\nEmpate!")
