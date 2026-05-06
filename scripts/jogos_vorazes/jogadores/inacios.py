import random

def estrategia(vida, num_jogadores_vivos, rodada):
    # Se estiver no duelo final
    if num_jogadores_vivos == 2:

        # Se estiver muito fraco, alterna entre curar, defender e atacar.
        if vida <= 25:
            if rodada % 3 == 0:
                return "curar"
            elif rodada % 3 == 1:
                return "defender"
            else:
                return "atacar"
            
        # Se estiver com vida baixa no duelo final, defende às vezes, mas ataca mais.
        elif vida <= 45:
            if rodada % 4 == 0:
                return "defender"
            else:
                return "atacar"

        # Se estiver bem de vida no duelo final, ataca.
        else:
            return "atacar"

    # Se ainda houver muitos jogadores e a vida estiver baixa, protege contra ataques em massa.
    if num_jogadores_vivos >= 4 and vida <= 55:
        if rodada % 2 == 0:
            return "defender"
        else:
            return "curar"

    # Se a vida estiver muito baixa, tenta recuperar.
    if vida <= 30:
        if rodada % 2 == 0:
            return "curar"
        else:
            return "defender"

    # Se a vida estiver média, defende às vezes, mas não sempre.
    if vida <= 50:
        if rodada % 3 == 0:
            return "defender"
        else:
            return "atacar"

    # Se houver muitos jogadores e a vida estiver boa, tenta atacar todos.
    if num_jogadores_vivos >= 4 and vida >= 75 and rodada % 5 == 0:
        return "atacar_todos"

    # Às vezes se defende por segurança.
    if random.random() < 0.20:
        return "defender"

    # No padrão, ataca.
    return "atacar"