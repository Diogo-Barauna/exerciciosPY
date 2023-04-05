v = 1
while v > 0:
    print(30 * '-')
    v = int(input('Quer ver a tabuada de qual valor? '))
    if v <= 0:
        print('Encerrando calculadora')
        break
    print(30 * '-')
    for c in range (1, 11):
        print ('{} x {} = {}'.format(v, c, v *c))
        