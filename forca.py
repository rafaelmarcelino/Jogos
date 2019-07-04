from os import open


def jogar():
    cabecalho_1 = 50 * "*"
    cabecalho_2 = "Bem vindos ao jogo de forca"

    mensagem_fim_jogo_acerto = "Parabéns você acertou a palavra secreta {}."
    mensagem_fim_jogo_erro = "Que pena. Você excedeu o número de tentativas. A palavra secreta era {}"
    mensagem_requisita_palpite = "Digite uma letra = "
    mensagem_palpite_encontrado = "Letra {} encontrada na posição {}"
    mensagem_qtd_letras_faltando = "Faltam {} letras para descobrir a palavra secreta"
    mensagem_tentativas_restante = "Ainda lhe restam {} tentativas."

    palavra_secreta = "anticonstitucionalissimamente".upper()
    letra_escondida = '_'
    palavra_descobrindo = [letra_escondida for letra in palavra_secreta]

    caminho_arquivo_palavras = "palavras.txt"
    arquivo = open(caminho_arquivo_palavras,)

    tentativas = len(palavra_secreta)#* 2

    enforcado = False
    acertou = False

    print(cabecalho_1)
    print(cabecalho_2)
    print(cabecalho_1)

    print(palavra_descobrindo)

    while( not enforcado and not acertou):
        palpite = input(mensagem_requisita_palpite).strip().upper()

        if(palpite in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(palpite == letra):
                    print(mensagem_palpite_encontrado.format(letra,index+1))
                    palavra_descobrindo[index] = letra
                index = index + 1

            print(palavra_descobrindo)
            print(mensagem_tentativas_restante.format(tentativas))

            if(palavra_descobrindo.count(letra_escondida)!= 0):
                print(mensagem_qtd_letras_faltando.format(palavra_descobrindo.count(letra_escondida)))
            else:
                print(mensagem_fim_jogo_acerto.format(palavra_secreta))
                acertou = True
        else:
            print(palavra_descobrindo)
            print(mensagem_tentativas_restante.format(tentativas))
            if(tentativas == 0):
                print(mensagem_fim_jogo_erro.format(palavra_secreta))
                enforcado = True
        tentativas -= 1


#Checking if the module was calling direct by processor
if(__name__ == "__main__"):
    jogar()