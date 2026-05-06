def estrategia(vida, num_jogadores_vivos, rodada):
    if vida > 50:
        return 'atacar'
    if vida > 80:
        return 'atacar_todos'
    elif num_jogadores_vivos > 5:
        return 'curar'
    elif num_jogadores_vivos > 3:
        return 'curar'
    else:
        return 'atacar'
