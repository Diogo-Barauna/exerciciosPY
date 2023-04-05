mai = 0
men = 0

for c in range (1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        mai = peso
        men = peso
    elif peso > mai:
        mai = peso
    elif peso < men:
        men = peso
print ("O maior peso lido foi {}".format(mai))
print ("O menor peso lido foi {}".format(men))