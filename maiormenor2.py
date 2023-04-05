n = cont = soma = media = 0
res = ''
while res != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    res = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / cont
print ('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))
