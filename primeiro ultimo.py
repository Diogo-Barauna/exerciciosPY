nome = str(input('Digite seu nome completo: ')).strip()
nom = nome.split()
print ('Seu primeiro nome é {}'.format(nom[0]))
print ('Seu último nome é {}'.format(nom[len(nom)-1]))
