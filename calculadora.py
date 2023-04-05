def soma ():
    print(17 * '-')
    n1 = int (input ('Digite o primeiro valor: '))
    n2 = int (input ('Digite o segundo valor: '))
    soma = n1 + n2
    print ('O resultado é:',soma)
    

def mult ():
    print(17 * '-')
    n1 = int (input ('Digite o primeiro valor: '))
    n2 = int (input ('Digite o segundo valor: '))
    mult = n1 * n2
    print ('O resultado é:',mult)
    

def sub ():
    print(17 * '-')
    n1 = int (input ('Digite o primeiro valor: '))
    n2 = int (input ('Digite o segundo valor: '))
    sub = n1 - n2
    print ('O resultado é:',sub)
   
    

def div ():
    print(17 * '-')
    n1 = int (input ('Digite o primeiro valor: '))
    n2 = int (input ('Digite o segundo valor: '))
    div = n1 / n2
    print ('O resultado é:',div)
   

c = 1

while c == 1:
    print(17 * '-')
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicaçaõ")
    print("4 - Divisão")
    print ("5 - Sair")
    print(17 * '-')
    escolha = int(input ('Selecione uma operação: '))

    if escolha == 1:
        soma()
    elif escolha == 2:
        sub()
    elif escolha == 3:
        mult()
    elif escolha == 4:
        div()
    elif escolha == 5:
        print('Desligando o sistema, até mais!')
        break 
    else:
        print('Escolha Inválida')



