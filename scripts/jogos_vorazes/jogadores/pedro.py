import random

# Função que define a estratégia do Pedro
def estrategia(vida, num_jogadores_vivos, rodada):
    if vida > 50:
        return "defender"
    else:
        return "atacar"

