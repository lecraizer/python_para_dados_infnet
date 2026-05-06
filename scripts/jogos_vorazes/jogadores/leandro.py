def estrategia(vida, num_jogadores_vivos, rodada):
    if vida >= 80:
        if num_jogadores_vivos > 3:
            return "atacar_todos"
        return "atacar"

    if vida >= 55:
        return "atacar"

    if vida >= 30:
        if num_jogadores_vivos <= 2:
            return "atacar"
        if num_jogadores_vivos > 3:
            return "defender"
        return "defender"

    if num_jogadores_vivos <= 2:
        return "atacar"

    return "defender"