import unicodedata
import random
import listas
import time


def Menu():
    escolha = input('1. Jogar\n2. Tutorial\n')
    if escolha == "1":
        Temp()
    elif escolha == "2":
        print("""
        Antes de inciar a partida, o jogador deverá escolher o tempo de duração do jogo.\n
        Assim que o tempo for escolhido, a partida irá iniciar automaticamente.\n
        O objetivo do jogo é advinhar o país através de 5 dicas(Continente, Área, População, Capital e Idioma).\n
        A cada dica apresentada, o jogador terá um palpite (fiquem atentos com a escrita).\n
        Toda vez que acertar um palpite, o jogador recebrá uma pontuação de acordo com as dicas utilizadas.\n
        Ao final do tempo de jogo, o jogador irá receber uma pontuação total, de acordo com os acertos obtidos.\n
        \n
        Para jogar, precione o núemro 1.
        """)
        Menu()


#A função "Tirar_Acento" irá padronizar todas os palpites sem acento, independente da maneira que o palpite for escrito"
def Tirar_Acento(Palpite): 
    Palpite = unicodedata.normalize("NFD", Palpite)
    Palpite = Palpite.encode("ascii","ignore")
    Palpite = Palpite.decode("utf-8")
    return Palpite


#A função "temp" irá solictar o tempo de jogo para o usuário e executará o jogo de acordo com o tempo escolhido.       
def Temp():
    soma_pontos = 0
    tempo = input("Quanto tempo você quer que tenha o jogo?\n[A] 1 Minuto.\n[B] 3 Minutos.\n[C] 5 Minutos.\n").upper()
    if tempo == "A":
        t1 = 1
        tempo = time.time() + t1 * 60
    elif tempo == "B":
        t1 = 3
        tempo = time.time() + t1 * 60
    elif tempo == "C":
        t1 = 5
        tempo = time.time() + t1 * 60
    else:
        print('Valor inválido. Digite a opção desejada: A, B ou C.')
        Temp()
    
    while tempo > time.time():
        soma_pontos += Jogo()
        if tempo < time.time():
            if soma_pontos >= 2:
                print(f'Acabou o tempo. A sua pontuação foi {soma_pontos} pontos em {t1} minutos.')
                break
            else:
                print(f'Acabou o tempo. A sua pontuação foi {soma_pontos} ponto em {t1} minutos.')
                break


    
#A função "jogo" define, de forma aleatória, qual será a senha da partida, bem como executa o jogo por completo. Informa as dicas ao jogador e calcula a pontuação de cada partida.
def Jogo():
    x = random.randint(0,202)
    senha = listas.SENHA[x]
    lista = [f'Continente: {listas.CONTINENTE[x]}', f'Área: {"{:,}".format(listas.AREA[x]).replace(",", ".")} km²', f'População: {"{:,}".format(listas.POPULACAO[x]).replace(",", ".")} habitantes', f'Capital: {listas.CAPITAL[x]}', f'Idioma: {listas.IDIOMA [x]}']
    pontos = 6
    Palpite = ""
    while senha != Palpite:
        for l in lista:
            pontos -= 1
            print(l)
            Palpite = Tirar_Acento(str(input("Digite um país: ")).upper())
            while Palpite not in listas.SENHA:
                print('Palpite inválido(Escrito errado). Tente outra vez.')
                Palpite = Tirar_Acento(str(input("Digite um país: ")).upper())
            if Palpite == senha:
                print(f'Parabéns! Você acertou o país. {senha.upper()}.\nA sua pontuação foi de {pontos} pontos.\n')
                return pontos
                break
            elif pontos == 1:
                pontos -= 1
                print(f'Você perdeu. O país correto era {senha.upper()}.\n')
                return pontos

        break


if __name__ == '__main__':
    Menu()