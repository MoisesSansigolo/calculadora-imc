peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está no pesso ideal')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
elif imc > 40:
    print('Voce está com OBESIDADE MORBIDA, cuidado')
    

    