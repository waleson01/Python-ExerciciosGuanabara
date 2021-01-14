peso = float(input('Digite o Peso: '))
altura = float(input('Digite a Altura: '))

imc = peso / (altura ** 2)

print('Seu IMC é de: {:.2f} '.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Parabéns! você esta no peso ideal!')
elif 25 < imc <= 30:
    print ('Você está no sobrepeso.')
elif imc >= 30 and imc <= 40:
    print ('Você está com obesidade.')
elif imc > 40:
    print('Obesidade Morbida.')
