nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

