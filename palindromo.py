frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
print('Você digitou a frase {}'.format(junto))
inverso = ''
for l in range (len(junto) - 1, -1, -1 ):
    inverso += junto[l]

print ('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Essa frase É um palíndromo')
else:
    print('Essa frase NÃO é um palíndromo')