preco = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão
[ 5 ] cancelar''')
escolha = int(input('Selecione uma opção: '))

if escolha == 1:
    desc = (preco * 10) / 100
    precoat = preco - desc
elif escolha == 2:
    desc = (preco * 5) / 100
    precoat = preco - desc
elif escolha == 3:
    precoat = preco
elif escolha == 4:
    par = int(input('Em quantas vezes quer parcelar? '))
    juros = (preco * 20) / 100
    precoat = juros + preco
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(par, precoat / par))
elif escolha == 5:
    print('Compra cancelada')
    exit()

print('Sua compra de R${} vai custar R${} no final.'.format(preco, precoat))