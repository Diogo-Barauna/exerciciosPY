import random
print(12 * '-=')
print('      ÍMPAR OU PAR')
print(12 * '-=')
v = int(input('Digite um valor: '))
pi = str(input('Ímpar ou par? [P/I] ')).upper()
vp = random.randint(1, 10)
total = v + vp
if total % 2 == 1:
    res = 'ímpar'
else:
    res = 'par'
print (25 * '-')
print('Você jogou {} e o computador {}. total de {} deu {}'.format(v, vp, total,res))
print (25 * '-')
if pi == 'I' and total % 2 == 1 or pi == 'P' and total % 2 == 0 :
    print('Você venceu!!')
else:
    print('Você perdeu :(')