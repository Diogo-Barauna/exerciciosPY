def tabuada(n):
    for c in range (1, 11):
        print ('{} x {:2} = {}'.format(n, c, n *c))
        print('-' * 12)

n = int (input ('Digite o número: '))
tabuada(n)