from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year 
idade = ano - nasc

if idade < 100:
    print('Você tem {} anos atualmente'.format(idade))
    if idade < 18:
        res = 18 - idade
        print('Ainda faltam {} anos para o seu alistamento'.format(res))
        print('Seu alistamento será no ano de {}'.format(res + ano))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    else:
        atraso = idade - 18
        print('Seu alistamento deveria ter sido em {} e está atrasado em {} anos'.format(ano - atraso, atraso))
else: 
    print('Idade inválida')
