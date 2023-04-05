print('Gerador de PA')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
tm = 1
termos = 0
while c <= 10:
    print(t, ' ->  ', end='')
    t += r
    c += 1

c = 1
print ('PAUSA')

while tm != 0:
    tm = int(input('Quantos termos você quer mostrar a mais? '))
    termos += tm
    c = 1
    while c <= tm:
        t += r 
        print(t - r, ' ->  ' if c < tm else ' -> PAUSA \n', end='')
        c += 1
termos += 10
print('Progressão finalizada com {} termos mostrados'.format(termos))
        
