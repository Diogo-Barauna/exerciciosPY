t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))

#Verificando o tipo do triângulo
if t1 == t2 == t3:
    tipo = ('EQUILÁTERO')
elif t1 == t2  or t1 == t3 or t3 == t2:
    tipo = ('ISÓRCELES')
elif t1 != t2 != t3:
     tipo = ('ESCALENO')

#Verificando se é possivel a formação do triângulo
if t1 + t2 > t3 and t2 + t3 > t1 and t3 + t1 > t2:
    print('Os segmentos acima PODEM formar um triângulo do tipo {}'.format(tipo))
else:
    print('Os segmentos acima NÃO podem formar um triângulo')
 

