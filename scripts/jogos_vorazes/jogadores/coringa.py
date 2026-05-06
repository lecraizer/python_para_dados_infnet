import random

def estrategia(vida, num_jogadores_vivos, rodada):
    # criar coringa, randomizar a estratégia de ataque, defesa, atacar todos ou cura
    return random.choice(["atacar", "defender", "atacar_todos", "curar"])