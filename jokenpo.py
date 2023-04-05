from random import choice
import os
from time import sleep
res = 'S'
vit = 0
vitpc = 0
while res != 'N':
    print('''    Faça sua jogada!
    [ 1 ] - Pedra
    [ 2 ] - Papel 
    [ 3 ] - Tesoura''')
    escolha = int(input('    Escolha: '))
    if escolha == 1:
        jogada = 'Pedra'
    elif escolha == 2:
        jogada = 'Papel'
    elif escolha == 3:
        jogada = 'Tesoura'
    else:
        print('\n    Escolha inválida')
        sleep(1)
        os.system('cls')
        continue
            
    pc = ['Pedra', 'Papel', 'Tesoura']
    jogadapc = choice(pc)
    sleep(0.5)
    print('\nSeu oponente escolheu {} e você {}\n'.format(jogadapc, jogada))
    sleep(0.5)
    if escolha == 1 and jogadapc == 'Tesoura' or escolha == 2 and jogadapc == 'Pedra' or escolha == 3 and jogadapc == 'Papel':
        print('                {}{}{}\n'.format('\033[32m', 'VOCÊ VENCEU!!','\033[m'))
        vit = vit + 1
    elif escolha == 1 and jogadapc == 'Papel' or escolha == 2 and jogadapc == 'Tesoura' or escolha == 3 and jogadapc == 'Pedra':
        print ('\033[31m               VOCÊ PERDEU :C \033[m \n')
        vitpc = vitpc + 1
    else:
        print('\033[34m                 EMPATE!\033[m \n')

    print('Você está com {}{}{} vitórias'.format('\033[33m',vit,'\033[m'))
    print('O computador está com {}{}{} vitórias\n'.format('\033[33m',vitpc,'\033[m'))
    res = str(input('Jogar novamente? S/N: ')).upper()
    if res == 'N':
        print('Obrigado por jogar, até a próxima!')
        break
    sleep(0.5)
    os.system('cls')