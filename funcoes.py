import unicodedata
import random
import listas

def tirar_acento(Palpite):
    Palpite = unicodedata.normalize("NFD", Palpite)
    Palpite = Palpite.encode("ascii","ignore")
    Palpite = Palpite.decode("utf-8")
    return Palpite


def jogo():
    x = random.randint(0,202)
    senha = listas.SENHA[x]
    continente = listas.CONTINENTE[x]
    area = listas.AREA[x]
    populacao = listas.POPULACAO[x]
    capital = listas.CAPITAL[x]
    idioma = listas.IDIOMA [x]
    lista = [continente, area, populacao, capital, idioma]
    pontos = 6
    Palpite = ""
    while senha != Palpite:
        for l in lista:
            pontos -= 1
            print('A dica é: ', l )
            Palpite = tirar_acento(str(input("Digite um país: ")).upper())
            if Palpite == senha:
                print(f'Parabéns! Você acertou o país. {senha.upper()}.\nA sua pontuação foi de {pontos} pontos.')
                break
            elif pontos == 1:
                pontos -= 1
                print(f'Você perdeu. O país correto era {senha.upper()}.')
        break        
            