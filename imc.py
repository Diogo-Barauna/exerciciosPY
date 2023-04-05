peso = int(input('Qual seu peso atual? (Kg): '))
altura = float(input('Qual sua altura? (m): '))
imc = peso / (altura ** 2)

print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está em sobrepeso')
elif imc >=30 and imc < 40:
    print('Você está em obesidade')
elif imc > 40:
    print('Você está em obesidade mórbida')