val = int(input('Valor da casa: R$'))
sal = int(input('Salário do comprador: R$'))
fin = int(input('Quantos anos de financiamento? '))

prest = val / (fin * 12)

print('Para comprar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(val, fin, prest))

if prest > (sal * 30)/100:
    print('O empréstimo foi NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO')
