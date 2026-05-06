import random


def estrategia(vida, num_jogadores_vivos, rodada):
    opcoes = ["curar", "atacar"]

    if vida > 50:
        return "defender"
    else:
        return random.choice(opcoes)
    