print(24*'-')
print('      Cadastre uma pessoa')
print(24*'-')
res = ''
maior = 0
h = 0
m = 0
while res != 'N':
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print(24*'-')
    
print('Total de pessoas com mais de 18 anos: {}'.format(maior))
print('Ao todo temos {} homens cadastrados'.format(h))
print('E temos {} mulheres com menos de 20 anos'.format(m))