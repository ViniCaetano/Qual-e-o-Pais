import unicodedata
import random
import listas
import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def get (self):
        return time.time() - self.start

def tirar_acento(Palpite):
    Palpite = unicodedata.normalize("NFD", Palpite)
    Palpite = Palpite.encode("ascii","ignore")
    Palpite = Palpite.decode("utf-8")
    return Palpite

        
def temp():
    tempo = input("Quanto tempo você quer que tenha o jogo?\n[A] 3 Minutos.\n[B] 5 Minutos.\n[C] 10 Minutos.\n").upper()
    if tempo == "A":
        tempo = 180
    elif tempo == "B":
        tempo = 300
    elif tempo == "C":
        tempo = 600
    else:
        print('Valor inválido. Digite a opção desejada: A, B ou C.')
        execucao()

def jogo():
    soma_pontos = 0
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
            if Palpite in listas.SENHA:
                if Palpite == senha:
                    print(f'Parabéns! Você acertou o país. {senha.upper()}.\nA sua pontuação foi de {pontos} pontos.')
                    soma_pontos += pontos
                    break
                elif pontos == 1:
                    pontos -= 1
                    print(f'Você perdeu. O país correto era {senha.upper()}.')
            else:
                l -= 1
                pontos += 1
                print("Nome do país incorreto. Digite novamente.")
        jogo()

def execucao():
    soma_pontos = 0
    t1 = temp()
    t2 = Timer()
    while tempo > t2:
        jogo()