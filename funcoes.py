import unicodedata
import random
import listas
import time


def tempo():
    t = input('Qual o tempo de jogo?\n[A] 1 minuto\n[B] 3 minutos\n[C] 5 minutos\n').upper()
    if t == 'A':
        return 60
    elif t == 'B':
        return 180
    elif t == 'C':
        return 300
    else:
        print('Escolha uma opção válida.')
        tempo()



def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    soma_pontos = 0
    while t:
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
                    soma_pontos += pontos
                    break
                elif pontos == 1:
                    pontos -= 1
                    print(f'Você perdeu. O país correto era {senha.upper()}.')
            break        

        
def tirar_acento(Palpite):
    Palpite = unicodedata.normalize("NFD", Palpite)
    Palpite = Palpite.encode("ascii","ignore")
    Palpite = Palpite.decode("utf-8")
    return Palpite


def jogo(countdown):
    soma_pontos = 0
    while countdown:
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
                    soma_pontos += pontos
                    break
                elif pontos == 1:
                    pontos -= 1
                    print(f'Você perdeu. O país correto era {senha.upper()}.')
            break        
            