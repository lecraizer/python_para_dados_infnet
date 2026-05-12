import random

# Função que define a estratégia do Carlos
def estrategia(vida, num_jogadores_vivos, rodada):
    if vida > 80:
        return "atacar"
    else:
        return "defender"

