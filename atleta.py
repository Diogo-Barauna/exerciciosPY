from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Atleta mirim')
elif idade > 9 and idade <= 14:
    print('Atleta infantil')
elif idade > 14 and idade <= 19:
    print('Atleta junior')
elif idade > 19 and idade <= 25:
    print('Atleta sênior')
else:
    print('Atleta master')
    