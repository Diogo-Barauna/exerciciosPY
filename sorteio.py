from random import choice

numero = list()
res = 'S'
while res != 'N':
    for c in range (1, 11):
        numero.append(c)

    escolhido = choice(numero)
    escolha = int(input('Digite um número de 1 a 10: '))

    if escolhido == escolha:
        print ('Você acertou o número, parabéns!!')
        
    else:
        print('Você errou, o número sorteado foi',escolhido)

    res = str(input('Tentar novamente? S/N ')).upper()
    if res == 'N':
        print('Obrigado por jogar, até mais!')
