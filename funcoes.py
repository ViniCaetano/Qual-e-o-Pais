import unicodedata
import random
import listas
import time


def tirar_acento(Palpite):
    Palpite = unicodedata.normalize("NFD", Palpite)
    Palpite = Palpite.encode("ascii","ignore")
    Palpite = Palpite.decode("utf-8")
    return Palpite

        
def temp():
    soma_pontos = 0
    tempo = input("Quanto tempo você quer que tenha o jogo?\n[A] 3 Minutos.\n[B] 5 Minutos.\n[C] 10 Minutos.\n").upper()
    if tempo == "A":
        tempo = time.time() + 180
    elif tempo == "B":
        tempo = time.time() + 300 
    elif tempo == "C":
        tempo = time.time() + 600
    else:
        print('Valor inválido. Digite a opção desejada: A, B ou C.')
        temp()
    while tempo > time.time():
        soma_pontos += jogo()
        if tempo < time.time():
            if soma_pontos >= 2:
                print(f'Acabou o tempo. A sua pontuação foi {soma_pontos} pontos.')
                break
            else:
                print(f'Acabou o tempo. A sua pontuação foi {soma_pontos} ponto.')
                break


    

def jogo():
    x = random.randint(0,202)
    senha = listas.SENHA[x]
    lista = [listas.CONTINENTE[x], listas.AREA[x], listas.POPULACAO[x], listas.CAPITAL[x], listas.IDIOMA [x]]
    pontos = 6
    Palpite = ""
    while senha != Palpite:
        for l in lista:
            pontos -= 1
            print('A dica é: ', l )
            Palpite = tirar_acento(str(input("Digite um país: ")).upper())
            if Palpite == senha:
                print(f'Parabéns! Você acertou o país. {senha.upper()}.\nA sua pontuação foi de {pontos} pontos.')
                return pontos
                break
            elif pontos == 1:
                pontos -= 1
                print(f'Você perdeu. O país correto era {senha.upper()}.')
                return pontos

        break