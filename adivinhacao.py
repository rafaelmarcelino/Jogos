import random

def jogar():
    total_de_tentativas = 0
    limite_min_palpite = 1
    limite_max_palpite = 100
    pontuacao_jogador = 1000


    cabecalho_1 = 50* "*"
    cabecalho_2 = "Bem vindos ao jogo de adivinhação"

    mensagem_solicitacao = "Digite um número para verificação = "
    mensagem_acerto = "Parabéns, você acertou. Sua pontuação é de {} pontos."
    mensagem_fim_jogo_erro = "Ah não, suas tentativas acabaram. Sua pontuação é de {} pontos"
    mensagem_erro_menor = "Que pena, você errou pois palpitou um número menor que o correto"
    mensagem_erro_maior = "Que pena, você errou pois palpitou um número maior que o correto"
    mensagem_fim_jogo = "Fim do jogo"
    mensagem_escolha_nivel = "Escolha o nível do jogo. 1 = fácil / 2 = médio / 3 = difícil -> "
    mensagem_escolha_nivel_errada = "Nivel inexistente. Jogo encerrando"

    print(cabecalho_1)
    print(cabecalho_2)
    print(cabecalho_1)

    numero_secreto = random.randrange(limite_min_palpite,limite_max_palpite+1)

    nivel_joogo = int(input(mensagem_escolha_nivel))
    if(nivel_joogo == 1):
        total_de_tentativas = 20
    elif(nivel_joogo == 2):
        total_de_tentativas = 10
    elif(nivel_joogo == 3):
        total_de_tentativas = 5
    else:
        total_de_tentativas = - 1
        print(mensagem_escolha_nivel_errada)

    for rodadas in range(1,total_de_tentativas + 1):
        print("Número secreto = {}".format(numero_secreto))
        print("Rodada {} de {} tentativas".format(rodadas,total_de_tentativas))
        palpite  = int(input(mensagem_solicitacao))

        if(palpite < limite_min_palpite or palpite > limite_max_palpite):
            print("Favor palpitar números entre {} e {}.".format(limite_min_palpite, limite_max_palpite))
            continue

        acerto = palpite == numero_secreto
        erro_menor = palpite < numero_secreto
        erro_maior = palpite > numero_secreto
        pontuacao_jogador = pontuacao_jogador - (abs(palpite - numero_secreto))

        if(acerto):
            print(mensagem_acerto.format(pontuacao_jogador))
            break
        else:
            if(erro_menor):
                print(mensagem_erro_menor)
            elif(erro_maior):
                print(mensagem_erro_maior)

            if(total_de_tentativas == rodadas):
                print(mensagem_fim_jogo_erro.format(pontuacao_jogador))

    print(mensagem_fim_jogo)

#Checking if the module was calling direct
if(__name__ == "__main__"):
    jogar()