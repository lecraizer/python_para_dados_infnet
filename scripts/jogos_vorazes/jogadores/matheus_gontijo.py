def estrategia(vida, num_jogadores_vivos, rodada):

    total_inicial = num_jogadores_vivos
    if num_jogadores_vivos < total_inicial:
        return "atacar"
    else:
        return "defender"
    