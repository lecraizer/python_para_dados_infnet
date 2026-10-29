# Pacotes gerais
import random
import time
import os
import importlib

# Função para criar um jogador
def criar_jogador(nome, estrategia_func):
    return {
        "nome": nome,
        "vida": 99,
        "morto": False,
        "defesa": False,
        "estrategia_func": estrategia_func,
        "bonus_ataque": 1.0
    }

# Carrega automaticamente todos os jogadores da pasta jogadores/
def nome_jogador(nome_arquivo):
    nome = nome_arquivo.replace(".py", "")
    partes = nome.split("_")
    return " ".join(parte.title() for parte in partes)


def carregar_jogadores():
    jogadores = []

    for arquivo in os.listdir("jogadores_alunos"):

        if not arquivo.endswith(".py"):
            continue

        if arquivo == "__init__.py":
            continue

        nome_modulo = arquivo[:-3]

        try:
            modulo = importlib.import_module(f"jogadores_alunos.{nome_modulo}")

            jogadores.append(
                criar_jogador(
                    nome_jogador(arquivo),
                    modulo.estrategia
                )
            )

        except Exception as e:
            print(f"Erro ao carregar {arquivo}: {e}")

    return jogadores


# Função para aplicar dano a um jogador
def receber_dano(jogador, dano):

    if jogador['defesa']:
        dano = dano // 5
        jogador['defesa'] = False

    if jogador['vida'] > 0:
        jogador['vida'] -= dano

        if jogador['vida'] <= 0:
            jogador['vida'] = 0
            jogador['morto'] = True
            print(f"\nO jogador {jogador['nome']} morreu.")


# Função para realizar um ataque
def atacar(jogador, alvo):

    dano = random.randint(1, 6) * jogador['bonus_ataque']
    dano = int(dano)

    receber_dano(alvo, dano)

    if alvo['vida'] <= 0:

        jogador['bonus_ataque'] += 0.2
        jogador['bonus_ataque'] = round(jogador['bonus_ataque'], 1)

        print(f"O jogador {jogador['nome']} matou o jogador {alvo['nome']}")
        print(f"{jogador['nome']} foi a {jogador['bonus_ataque']:.1f} de dano")


# Função para ativar a defesa
def defender(jogador):
    jogador['defesa'] = True


# Função para curar
def curar(jogador):

    jogador['vida'] += random.randint(1, 2)

    if jogador['vida'] > 99:
        jogador['vida'] = 99


# Ataque em área
def atacar_todos(jogador, jogadores, p=0.2):

    if random.random() < p:

        for alvo in [j for j in jogadores if j != jogador and not j['morto']]:
            atacar(jogador, alvo)


# Evento de cerco
def cerco(jogadores, rodada):

    vivos = [j for j in jogadores if not j['morto']]

    if not vivos:
        return

    alvo = random.choice(vivos)

    dano_aleatorio = int(random.randint(4, 6) * (rodada / 200))

    alvo['vida'] -= dano_aleatorio

    print(
        f"\nO jogador {alvo['nome']} recebeu um dano aleatório de "
        f"{dano_aleatorio} pelo cerco.".rjust(35)
    )

    if alvo['vida'] <= 0:

        alvo['vida'] = 0
        alvo['morto'] = True

        print(f"O jogador {alvo['nome']} morreu devido ao cerco.")


# Realiza a ação de um jogador
def realizar_acao(jogador, jogadores, rodada, rank):

    if jogador['morto']:
        return

    estrategia = jogador['estrategia_func'](
        jogador['vida'],
        len([j for j in jogadores if not j['morto']]),
        rodada
    )

    if estrategia == "atacar":

        alvos = [j for j in jogadores if j != jogador and not j['morto']]

        if alvos:
            alvo = random.choice(alvos)
            atacar(jogador, alvo)

    elif estrategia == "defender":
        defender(jogador)

    elif estrategia == "atacar_todos":
        atacar_todos(jogador, jogadores)

    elif estrategia == "curar":
        curar(jogador)


# Função principal
def jogo():

    jogadores = carregar_jogadores()

    print("\nJogadores carregados:")

    for jogador in jogadores:
        print(f" - {jogador['nome']}")

    rodada = 1

    while len([j for j in jogadores if not j['morto']]) > 1:
        
        if rodada < 500:
            time.sleep(0.1)
        if rodada < 1000:
            time.sleep(0.05)
        elif rodada < 2000:
            time.sleep(0.02)
        else:
            time.sleep(0.07)

        if rodada % 100 == 0:

            print(f"\n\n--- Rodada {rodada} ---\n")

            jogadores = sorted(
                jogadores,
                key=lambda x: x['vida'],
                reverse=True
            )

            for jogador in jogadores:

                if not jogador['morto']:

                    print(
                        f"{jogador['nome']}: "
                        f"{jogador['vida']} HP | "
                        f"A: {jogador['bonus_ataque']}"
                        .rjust(35)
                    )

            cerco(jogadores, rodada)

        for jogador in jogadores:

            rank = jogadores.index(jogador)

            realizar_acao(
                jogador,
                jogadores,
                rodada,
                rank
            )

        rodada += 1

    vencedor = [j for j in jogadores if not j['morto']][0]

    print(
        f"\n{vencedor['nome']} venceu o jogo "
        f"com {vencedor['vida']} HP "
        f"na rodada {rodada}"
    )


# Executar
if __name__ == "__main__":
    jogo()



# Ataque ter uma probabilidade (ex. 10%) de ser um ataque crítico (1.5x)
# Probabilidade de escapar do cerco proporcional ao bonus de ataque
# Magnitude de cura proporcional ao bonus de ataque
# Eventos aleatórios ao longo do jogo
# Escolher uma classe (arqueiro, bárbaro, mago/fada, paladino)
# Criar arquivo de top cercos