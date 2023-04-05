from random import choice
numero = list()
tentativas = 0
escolha = ''
for c in range (1, 11):
    numero.append(c)
    escolhido = choice(numero)

print('Selecionei um número de 1 a 10, consgue adivinhar qual foi? ')
while escolha != escolhido:
    escolha = int(input('Digite um número: '))
    tentativas += 1
    if escolhido < escolha:
        print ('Menos, tente novamente')
    elif escolhido > escolha:
        print('Mais, tente novamente')
    elif escolhido == escolha:
        print('Você acertou com {} tentativas, parabéns!'.format(tentativas))