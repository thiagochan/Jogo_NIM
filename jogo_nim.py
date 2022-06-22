def partida():
    n = m = 0
    turnoComputador = True
    while (n <= 0 or m <= 0):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    
    pecasAgora = n

    if (n % (m + 1) == 0):
        turnoComputador = False
        print("Você começa!\n")
    else:
        turnoComputador = True
        print("Computador começa!\n")

    while (pecasAgora >= 1):
        if (turnoComputador):
            jogadaComputador = computador_escolhe_jogada(pecasAgora, m)

            if (pecasAgora - jogadaComputador == 0):
                print("Fim do jogo! O computador ganhou!")
                break

            pecasAgora -= jogadaComputador

            if (jogadaComputador == 1):
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", jogadaComputador, "peças.")

            print("Agora restam", pecasAgora, "peças no tabuleiro.\n")
            turnoComputador = False

        else:
            jogadaUsuario = usuario_escolhe_jogada(pecasAgora, m)

            if (pecasAgora - jogadaUsuario == 0):
                print("Fim do jogo! Você ganhou!")
                break

            pecasAgora -= jogadaUsuario

            if (jogadaUsuario == 1):
                print("Você tirou uma peça.\n")
            else:
                print("Você tirou ", jogadaUsuario, " peças.")
            
            print("Agora restam ", pecasAgora, " peças no tabuleiro.\n")
            turnoComputador = True

        


def computador_escolhe_jogada(n, m):
    jogadaComputador = 0

    for i in range(1, (m + 1)):
        if ((n - i) % (m + 1) == 0):
            jogadaComputador = i
            break
        else:
            jogadaComputador = m

    return jogadaComputador
    
def usuario_escolhe_jogada(n, m):
    jogadaUsuario = 0

    while (jogadaUsuario <= 0 or jogadaUsuario > m):
        jogadaUsuario = int(input("Quantas peças você vai tirar? "))

    return jogadaUsuario

partida()