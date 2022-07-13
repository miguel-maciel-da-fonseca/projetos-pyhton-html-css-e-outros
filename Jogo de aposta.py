import random
import time


def mensagem(msg):
    print('='*len(msg))
    print(msg)
    time.sleep(1)


def jogadores(j, i):
    for n in i:
        jogos.append(n)
        print(f'{j} jogou: {n}')
        time.sleep(1)


def maioral(i, j):
    maior = max(jogos)
    if maior == jogos[i]:
        maior = j


def troca(v, i, j):
    if v == i:
        v = j


saldo = 100
perda = vitória = 0
while True:
    print('\033[31m=\033[m'*20)
    print('      \033[33mCASSINO\033[m')
    print('\033[32m=\033[m'*20)

    jogador1 = [random.randint(1, 6)]
    jogador2 = [random.randint(1, 6)]
    jogador3 = [random.randint(1, 6)]
    jogador4 = [random.randint(1, 6)]

    print('Escolha um jogador:')
    print('''
    JOGADOR 1
    JOGADOR 2
    JOGADOR 3
    JOGADOR 4
    ''')
    a = int(input('\033[34mEscolha um: \033[m'))

    if a >= 5 or a <= 0:
        while a >= 5 or a <= 0:
            print('='*20)
            print('\033[32mNÃO TEMOS ESSE JOGADOR\033[m')
            print('='*20)
            print('ESCOLHA OUTRO')
            print('='*13)
            a = int(input('\033[34mEsolha um: \033[m'))
            print('='*13)
    aposta = (float(input('\033[34mQuanto vai apostar: R$\033[m')))
    print('='*20)

    while aposta > saldo:
        print('Você não possui esse saldo')
        aposta = (float(input('Quanto vai apostar: R$')))

    if aposta == saldo:
        print('\033[31m!Tem certeza que quer apostar tudo!\033[m')
        print('='*20)
        escolha1 = input('\033[32mSIM OU NÃO [S/N]\033[m').upper().strip()[0]
        print('='*20)

        while escolha1 == 'N':
            print('='*20)
            print('Escolha um jogador:')
            print('''
    JOGADOR 1
    jOGADOR 2
    JOGADOR 3
    JOGADOR 4
    ''')
            b = int(input('\033[34mEsolha um: \033[m'))

            if b >= 5 or b <= 0:
                while b >= 5 or b <= 0:
                    print('NÃO TEMOS ESSE JOGADOR')
                    print('='*24)
                    print('ESCOLHA OUTRO')
                    print('='*24)
                    b = int(input('Esolha um: '))
                    print('='*24)
            aposta = (float(input('\033[34mQuanto vai apostar: R$\033[m')))
            print('='*20)

            while aposta > saldo:
                print('Você não possui esse saldo')
                aposta = (float(input('Quanto vai apostar: R$')))
            if aposta == saldo:
                print('\033[31m!Tem certeza que quer apostar tudo!\033[m')
                print('='*20)
                escolha1 = input(
                    '\033[32mSIM OU NÃO [S/N]\033[m').upper().strip()[0]
                print('='*20)
            if escolha1 == 'S':
                a = b
                break

    jogos = []
    maior = 0

    jogadores('jogador 1', jogador1)
    jogadores('jogador 2', jogador2)
    jogadores('jogador 3', jogador3)
    jogadores('jogador 4', jogador4)

    maioral(0, 'jogador 1')
    maioral(1, 'jogador 2')
    maioral(2, 'jogador 3')
    maioral(3, 'jogador 4')

    troca(a, 1, 'jogador 1')
    troca(a, 2, 'jogador 2')
    troca(a, 3, 'jogador 3')
    troca(a, 4, 'jogador 4')

    if a == maior:
        print('='*20)
        saldo += aposta
        vitória += 1
        print('você ganhou')
        print(f'Seu saldo é de: R${saldo}')
        print('='*20)

    else:
        print('='*20)
        saldo -= aposta
        perda += 1
        print('você perdeu')
        print(f'Seu saldo é de: R${saldo}')
        print('='*20)

    if saldo == 0:
        print('\033[31mVocê não tem mais saldo!')
        print('   volte outra hora\033[m')
        break

    escolha = input('Quer continuar[S/N] ').upper().strip()[0]
    if escolha == 'N':
        break

mensagem(f'\033[32mVocê ganhou {vitória} \033[m')
mensagem(f'\033[31mVocê perdeu {perda} \033[m')
mensagem(f'Você saiu com saldo de {saldo} ')
print('='*28)
