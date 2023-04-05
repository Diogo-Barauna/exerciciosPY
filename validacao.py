sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino registrado!')
elif sexo == 'F':
    print('Sexo feminino registrado!')
else:
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo inválido, digite novamente [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            print('Sexo masculino registrado!')
        elif sexo == 'F':
            print('Sexo feminino registrado!')