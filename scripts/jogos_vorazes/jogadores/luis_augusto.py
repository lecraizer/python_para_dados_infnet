def estrategia(vida, num_jogadores_vivos, rodada):
    if vida < 15:
        return 'curar'
    elif num_jogadores_vivos <= 2:
        return 'atacar'
    elif vida > 60:
        return 'atacar'
    else:
        return 'defender'
