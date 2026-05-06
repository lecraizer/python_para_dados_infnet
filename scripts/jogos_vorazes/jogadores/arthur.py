import random

def estrategia(vida, num_jogadores_vivos, rodada):
    escolhas = ['atacar', 'atacar todos', 'curar']
    pesos = [5, 3, 2]

    if rodada < 10 and vida > 80:
        return 'atacar'
    elif num_jogadores_vivos > 3 and vida > 40 :
        return random.choices(escolhas, weights=pesos, k=1)[0]
