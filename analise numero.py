num = (input('Informe um número: '))
separa = list(str(num))

if len(separa) == 1:
    print('Unidade: ', separa[0])

elif len(separa) == 2:
    print('Unidade: ', separa[1])
    print('Dezena: ', separa[0])

elif len(separa) == 3:
    print('Unidade: ', separa[2])
    print('Dezena: ', separa[1])
    print('Centeta: ', separa[0])

elif len(separa) == 4:
    print('Unidade: ', separa[3])
    print('Dezena: ', separa[2])
    print('Centeta: ', separa[1])
    print('Milhar: ', separa[0])