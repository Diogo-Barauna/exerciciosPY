from datetime import date
maior = 0
menor = 0

for c in range (1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E {} pessoas menores de idade'.format(menor))