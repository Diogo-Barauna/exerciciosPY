maior = 0
esc = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while esc != 5:
    print('''        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
    esc = int(input('Escolha uma opção: '))
    if esc == 1:
        soma = n1 + n2
        print ('A soma dos números é {}'.format(soma))
    elif esc == 2:
        mult = n1 * n2
        print ('A multiplicação dos números é {}'.format(mult))
    elif esc == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        if n1 == n2:
            print('Os números são iguais')
        else:
            print ('O maior número é {}'.format(maior))
    elif esc == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif esc == 5:
        print ('Desligando o programa, até mais!')
        break
    else:
        print('Opção inválida')
