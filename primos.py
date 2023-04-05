num = int(input('Digite um número: '))
div = 0
for c in range (1, num + 1):
        if num % c == 0:
                div += 1
                print('({})'.format(c), end=" ")
        else:
                print(c, end=" ")

print('\nO número {} foi divisível {} vezes'.format(num,div))

if div > 2:
        print('Por isso ele NÃO é primo')
else:
        print('Por isso ele É primo')

        
