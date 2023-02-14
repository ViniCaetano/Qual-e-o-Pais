import unicodedata
import random
import listas
import time


def remover_acentos(palavra):
    palavra = unicodedata.normalize("NFD", palavra)
    palavra = palavra.encode("ascii","ignore")
    palavra = palavra.decode("utf-8")
    return palavra

    
def pedir_tempo():
    tempos = {"A": 1, "B": 3, "C": 5}
    opcao = input("Quanto tempo você quer que tenha o jogo?\n[A] 1 Minuto.\n[B] 3 Minutos.\n[C] 5 Minutos.\n").upper()
    if opcao in tempos:
        t = tempos[opcao]
        return t, time.time() + t * 60
    else:
        print('Valor inválido. Digite a opção desejada: A, B ou C.')
        return pedir_tempo()
    

def jogar_rodada(senha, dicas):
    pontos = 6
    while True:
        for dica in dicas:
            pontos -= 1
            print(dica)
            palpite = remover_acentos(input("Digite um país: ").upper())
            while palpite not in listas.SENHA:
                print('Palpite inválido (Escrito errado). Tente outra vez.')
                palpite = remover_acentos(input("Digite um país: ").upper())
            if palpite == senha:
                print(f'Parabéns! Você acertou o país. {senha.upper()}.\nA sua pontuação foi de {pontos} pontos.')
                return pontos
            elif pontos == 1:
                pontos -= 1
                print(f'Você perdeu. O País era {senha.upper()}')


if __name__ == '__main__':
    soma_pontos = 0
    pedir_tempo()
    while pedir_tempo() > time.time():
        soma_pontos += jogar_rodada()
        if pedir_tempo() < time.time():
            if soma_pontos >= 2:
                print(f'Acabou o tempo. A sua pontuação foi {soma_pontos} pontos em {t1} minutos.')
                break
            else:
                print(f'Acabou o tempo. A sua pontuação foi {soma_pontos} ponto em {t1} minutos.')
                break