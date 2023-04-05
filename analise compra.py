print (32*'-')
print ('          LAMBAI STORE')
print (32*'-')
total = caro = cont = 0
res = nomeb = ''
while res != 'N':
    cont += 1
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1:
        barato = preco
        nomeb = nome
    if preco < barato:
        barato = preco
        nomeb = nome
    res = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]
print (12*'-','FIM DO PROGRAMA', 12*'-')
print('O total da compra foi R${}'.format(total))
print('Temos {} produtos custando mais de R$1000.00'.format(caro))
print('O produto mais barato foi {} que custa R${}'.format(nomeb,barato))

