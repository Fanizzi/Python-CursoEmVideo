peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Você está abaixo do peso. Seu índice de massa corporal é de: {imc:.2f}')

elif imc > 18.5 and imc < 24.9:
    print(f'Sua classificação é Peso Normal, seu índice de massa corporal é de: {imc:.2f}')

elif imc > 25 and imc < 29.9:
    print(f'Sua classificação é Sobrepeso. Seu índice de massa corporal é de: {imc:.2f}')

elif imc > 30 and imc < 34.9:
    print(f'Sua classificação é de Obesidade Grau I. Seu índice d emassa corporal é de {imc:.2f}')

elif imc > 35 and imc < 39.9:
    print(f'Sua classificação é de Obesidade Grau II. Seu índice de massa corporal é de {imc:.2f}')

else:
    print(f'Sua classificação é de Obesidade Grau III. Seu índice de massa corporal é de {imc:.2f}')