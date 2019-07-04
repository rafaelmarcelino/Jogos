import  forca
import adivinhacao

cabecalho_1 = 50 * "*"
cabecalho_2 = "Bem vindos a seleção de jogos"
mensagem_selecao = "Jogar Advinhação (1) ====== Jogar Forca (2)"
mensagem_escolha = "Digite uma das opções -> "

print(cabecalho_1)
print(cabecalho_2)
print(cabecalho_1)

print(mensagem_selecao)

jogo_selecionado = int(input(mensagem_escolha))

if(jogo_selecionado == 1):
    adivinhacao.jogar()
elif (jogo_selecionado == 2):
    forca.jogar()

