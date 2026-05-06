import random

# Função que define a estratégia do Fernando
def estrategia(vida, num_jogadores_vivos, rodada):
    if vida > 40:
        return "atacar"
    elif vida < 15 and num_jogadores_vivos > 3:
        return "curar"
    else:
        return "defender"