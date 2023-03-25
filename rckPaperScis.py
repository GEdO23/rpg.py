# ROCK PAPER SCISSORS 
    # Jogo normal de Pedra Papel e Tesoura, em Python.
    # Pedra < Papel < Tesoura < Pedra

# ETAPAS
    # Perguntar ao Jogador se ele quer jogar Pedra[0], Papel[1] ou Tesoura[2]
    # Escolher um numero inteiro de 0 a 2 aleatório para jogada do Oponente
    # Mostrar resultado da batalha
        # Se Jogador ganhar, adcionar 1 ao SCORE
        # Se Jogador perder, remover 1 de 3 de VIDA
    # Perguntar ao jogador se ele quer continuar
        # Se SIM -> Repetir +1 vez
        # Se NAO -> Acabar o Jogo

import random

life = 3
score = 0

def playerTurn():
    plyr_move = int(input("Escolha seu movimento!\nPedra[0]\nPapel[1]\nTesoura[2]\n"))
    return plyr_move

def enemyTurn():
    enmy_move = random.randint(0, 2)
    return enmy_move

def convertion():
    if plyr_move == 0:
        plyr_move = "Pedra"
    elif plyr_move == 1:
        plyr_move = "Papel"
    elif plyr_move == 2:
        plyr_move = "Tesoura"

    if enmy_move == 0:
        enmy_move = "Pedra"
    elif enmy_move == 1:
        enmy_move = "Papel"
    elif enmy_move == 2:
        enmy_move = "Tesoura"

    return plyr_move, enmy_move

def results():
    if plyr_move == "Pedra":
        if enmy_move == "Papel":
            # Papel ganha de Pedra, logo, o Oponente venceu
            life -= 1
        elif enmy_move == "Tesoura":
            # Pedra ganha de Tesoura, logo, você venceu
            score += 1

    if plyr_move == "Papel":
        if enmy_move == "Tesoura":
            # Tesoura ganha de Papel, logo, o Oponente venceu
            life -= 1
        elif enmy_move == "Pedra":
            # Papel ganha de Pedra, logo, você venceu
            score += 1
    
    if plyr_move == "Tesoura":
        if enmy_move == "Pedra":
            # Pedra ganha de Tesoura, logo, o Oponente venceu
            life -= 1
        elif enmy_move == "Papel":
            # Tesour ganha de Papel, logo, você venceu
            score += 1
    return life, score

def repeat():
    repeat = input("Tentar novamente? (y/n)\n")
    if repeat == 'y':
        game()
    else:
        print("\nGAME OVER")

def game():
    playerTurn()
    enemyTurn()
    convertion()
    results()
    repeat()

game()