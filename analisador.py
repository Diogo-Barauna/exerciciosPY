fem = 0
masc = 0
soma = 0
mul = 0
vel = 0
for c in range (1,5):
    print ("---- {}° PESSOA ----".format(c))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    soma += idade
    sexo = str(input("Sexo[M/F]: "))
    if c == 1 and sexo == 'M':
        vel = idade
        older = nome
    if sexo == 'M' and idade > vel:
        vel = idade
        older = nome   
    if sexo == 'F' and idade < 20:
        mul += 1
        
med = soma / c
print ('A média de idade entre os grupos é de {} anos'.format(med))
print ('O homem mais velho tem {} anos e se chama {}'.format(vel, older))
print ('Ao todo são {} mulheres com menos de 20 anos'.format(mul))