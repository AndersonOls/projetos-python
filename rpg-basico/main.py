vida_heroi = 10
dano_heroi = 2
dano_inimigo = 1
vida_inimigo = 6


def batalha():
    global vida_heroi
    global vida_inimigo
    global dano_heroi
    global dano_inimigo

    while vida_heroi > 0:

        if vida_inimigo >= 2:
            print('Sua vida: %d | Vida do inimigo: %d' % (vida_heroi, vida_inimigo))

            escolha = int(input('Digite 1 para atacar ou 2 para fugir: '))

            if escolha == 1:
                print('Você atacou o seu adversário e ele sofreu %d de dano' % dano_heroi)
                vida_inimigo = vida_inimigo - dano_heroi
                print('Você sofreu um ataque e recebeu %d de dano' % dano_inimigo)
                vida_heroi = vida_heroi - dano_inimigo
            elif escolha == 2:
                print('Você gastou energia para correr, por isso perdeu 1 de vida')
                vida_heroi = vida_heroi - 1
                main()
                break

        elif vida_inimigo == 0:
            print('*** Você derrotou seu inimigo e encontrou uma poção! '
                  'Ganhou +1 de vida***')
            vida_heroi = vida_heroi + 1
            vida_inimigo = 6
            main()
            break


def main():
    print('Você encontrou um inimigo!')
    start = input('Deseja lutar? s ou n: ')

    if start == 's':
        batalha()
    elif start == 'n':
        print('Fim de jogo!')

main()