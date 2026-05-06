# Função que define a estratégia do João
def estrategia(vida, num_jogadores_vivos, rodada):
    if vida > 50:
        return 'atacar_todos'
    elif num_jogadores_vivos > 4:
        return 'curar'
    else:
        return 'atacar'