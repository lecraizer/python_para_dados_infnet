def estrategia(vida, num_jogadores_vivos, rodada):
    if num_jogadores_vivos <= 3:
        return 'atacar_todos'

    if vida > 60:
        return 'atacar'

    if 40 < vida < 50:
        return 'curar'

    if num_jogadores_vivos > 5:
        return 'defender'

    return 'defender'