import random

mensagem_fim_jogo_acerto = "Parabéns você acertou a palavra secreta."
mensagem_fim_jogo_erro = "Que pena. Você excedeu o número de tentativas. A palavra secreta era {}"
mensagem_requisita_palpite = "Digite uma letra = "
mensagem_palpite_encontrado = "Letra {} encontrada na posição {}"
mensagem_qtd_letras_faltando = "Faltam {} letras para descobrir a palavra secreta"
mensagem_tentativas_restante = "Ainda lhe restam {} tentativas."

READ = "r"
WRITE = "w"
#================================================================================================
#=========================================MÉTODOS LOCAIS=========================================
#================================================================================================

def imprime_cabecalho():
    cabecalho_1 = 50 * "*"
    cabecalho_2 = "Bem vindos ao jogo de forca"

    print(cabecalho_1)
    print(cabecalho_2)
    print(cabecalho_1)


def abre_arquivo_desejado(nome_arquivo,tipo_operacao):
    caminho_arquivo_palavras = nome_arquivo
    arquivo = open(caminho_arquivo_palavras, tipo_operacao)
    palavras_coletadas = []

    for linhas in arquivo:
        palavras_coletadas.append(linhas.strip().upper())
    arquivo.close()

    return palavras_coletadas


def escolhe_palavra_secreta(palavras_coletadas):
    index_busca_palavra = random.randrange(0, len(palavras_coletadas))
    palavra_secreta = palavras_coletadas[index_busca_palavra]
    return palavra_secreta

def atualiza_palavra_descobrindo(palavra_secreta,palpite,palavra_descobrindo):
    index = 0
    for letra in palavra_secreta:
        if (palpite == letra):
            print(mensagem_palpite_encontrado.format(letra, index + 1))
            palavra_descobrindo[index] = letra
        index = index + 1

    return palavra_descobrindo

def exibe_fim_jogo_erro(palavra_secreta):
        print(mensagem_fim_jogo_erro.format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def imprime_mensagem_vencedor():
    print(mensagem_fim_jogo_acerto)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

#================================================================================================
#========================================MÉTODO PRINCIPAL========================================
#================================================================================================


def jogar():

    palavras_coletadas =  abre_arquivo_desejado("palavras.txt",READ)
    palavra_secreta = escolhe_palavra_secreta(palavras_coletadas)

    letra_escondida = '_'
    palavra_descobrindo = [letra_escondida for letra in palavra_secreta]

    tentativas = len(palavra_secreta)

    enforcado = False
    acertou = False

    imprime_cabecalho()

    while( not enforcado and not acertou):
        palpite = input(mensagem_requisita_palpite).strip().upper()

        if(tentativas > 1):
            if(palpite in palavra_secreta):
                palavra_descobrindo = atualiza_palavra_descobrindo(palavra_secreta,palpite,palavra_descobrindo)
                print(palavra_descobrindo)
                print(mensagem_tentativas_restante.format(tentativas))

                if(palavra_descobrindo.count(letra_escondida)!= 0):
                    print(mensagem_qtd_letras_faltando.format(palavra_descobrindo.count(letra_escondida)))
                else:
                    imprime_mensagem_vencedor()
                    acertou = True
            else:
                tentativas -= 1
                print(palavra_descobrindo)
                print(mensagem_tentativas_restante.format(tentativas))
        else:
            exibe_fim_jogo_erro(palavra_secreta)
            enforcado = True


#Checking if the module was calling direct by processor
if(__name__ == "__main__"):
    jogar()