velocidade = float(input('Qual é a velociade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar a multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
