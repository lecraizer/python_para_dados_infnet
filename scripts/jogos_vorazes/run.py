# Pacotes gerais
import random
import time

# Módulos de jogadores
import jogadores.kamikaze as kamikaze
import jogadores.arriscado as arriscado
import jogadores.arthur as arthur
import jogadores.coringa as coringa
import jogadores.luis_augusto as luis_augusto
import jogadores.matheus_gontijo as matheus_gontijo
import jogadores.inacios as inacios
import jogadores.escudo as escudo
import jogadores.fada as fada
import jogadores.fernando as fernando
import jogadores.francisco_de_assis as francisco_de_assis
import jogadores.leandro as leandro
import jogadores.luan as luan
import jogadores.nicolas as nicolas


# Função para criar um jogador
def criar_jogador(nome, estrategia_func):
    return {
        "nome": nome,
        "vida": 99,  # Vida inicial
        "morto": False,
        "defesa": False,
        "estrategia_func": estrategia_func, # "atacar" ou "defender" ou "curar" ou "atacar_todos"
        "bonus_ataque": 1.0  # Bônus de ataque inicial
    }


# Função para aplicar dano a um jogador
def receber_dano(jogador, dano):
    if jogador['defesa']:  # Se o jogador estiver defendendo, recebe menos dano
        dano = dano // 5 # Inteiro da divisão de dano por 5
        jogador['defesa'] = False # Desabilitar a defesa após o dano ser recebido

    if jogador['vida'] > 0: # Se o jogador ainda estiver vivo
        jogador['vida'] -= dano  # Aplicar o dano
        if jogador['vida'] <= 0: # Se o jogador morreu devido ao dano
            jogador['vida'] = 0
            jogador['morto'] = True
            print(f"\nO jogador {jogador['nome']} morreu.")


# Função para realizar um ataque de um jogador a outro
def atacar(jogador, alvo):
    dano = random.randint(1, 6) * jogador['bonus_ataque']
    dano = int(dano)  # Converter para inteiro
    receber_dano(alvo, dano)

    if alvo['vida'] <= 0:
        jogador['bonus_ataque'] += 0.1
        jogador['bonus_ataque'] = round(jogador['bonus_ataque'], 1)
        print(f"O jogador {jogador['nome']} matou o jogador {alvo['nome']}")
        print(f"{jogador['nome']} foi a {jogador['bonus_ataque']:.1f} de dano")
        

# Função para ativar a defesa de um jogador
def defender(jogador):
    jogador['defesa'] = True

def curar(jogador):
    jogador['vida'] += random.randint(1, 2)
    if jogador['vida'] > 99:
        jogador['vida'] = 99


def atacar_todos(jogador, jogadores, p=0.2):
    # 20% de chance de atacar todos os jogadores
    if random.random() < p:
        for alvo in [j for j in jogadores if j != jogador and not j['morto']]:
            atacar(jogador, alvo)

def cerco(jogadores, rodada):
    alvo = random.choice([j for j in jogadores if not j['morto']]) # Escolhe um alvo aleatório que esteja vivo
    dano_aleatorio = int(random.randint(1, 3)*(rodada/200))
    alvo['vida'] -= dano_aleatorio
    print(f"\nO jogador {alvo['nome']} receber um dano aleatório de {dano_aleatorio} pelo cerco.".rjust(35))
    if alvo['vida'] <= 0:
        alvo['vida'] = 0
        alvo['morto'] = True
        print(f"O jogador {alvo['nome']} morreu devido ao cerco.")
    


# Função para realizar a ação de um jogador
def realizar_acao(jogador, jogadores, rodada, rank):
    if jogador['morto']: # Se o jogador estiver morto, não fazer nada
        return
    
    # Caso contrário, a função continua (não há necessidade do 'else' por causa do 'return')

    # Chama a função de estratégia do jogador, que recebe 3 parâmetros: vida do jogador, quantidade de jogadores vivos e rodada atual
    estrategia = jogador['estrategia_func'](jogador['vida'], len([j for j in jogadores if not j['morto']]), rodada)

    if estrategia == "atacar":
        alvo = random.choice([j for j in jogadores if j != jogador and not j['morto']])  # Escolhe um alvo aleatório
        atacar(jogador, alvo) # Alvo é um jogador (dicionário)
    elif estrategia == "defender":
        defender(jogador) # Ativa a defesa do jogador
    elif estrategia == "atacar_todos":
        atacar_todos(jogador, jogadores) # Atacar todos os jogadores com certa probabilidade
    elif estrategia == "curar":
        curar(jogador) # Cura a vida do jogador


# Função principal para rodar o jogo
def jogo():
    
    # Inicializa a lista de jogadores
    jogadores = []

    # Cria jogadores fictícios com suas respectivas estratégias
    jogadores.append(criar_jogador("Kamikaze", kamikaze.estrategia))
    jogadores.append(criar_jogador("Arriscado", arriscado.estrategia))
    jogadores.append(criar_jogador("Arthur", arthur.estrategia))
    jogadores.append(criar_jogador("Coringa", coringa.estrategia))
    jogadores.append(criar_jogador("Luis Augusto", luis_augusto.estrategia))
    jogadores.append(criar_jogador("Matheus Gontijo", matheus_gontijo.estrategia))
    jogadores.append(criar_jogador("Inácios", inacios.estrategia))
    jogadores.append(criar_jogador("Escudo", escudo.estrategia))
    jogadores.append(criar_jogador("Fada", fada.estrategia))
    jogadores.append(criar_jogador("Fernando", fernando.estrategia))
    jogadores.append(criar_jogador("Francisco de Assis", francisco_de_assis.estrategia))
    jogadores.append(criar_jogador("Leandro", leandro.estrategia))
    jogadores.append(criar_jogador("Luan", luan.estrategia))
    jogadores.append(criar_jogador("Nicolás", nicolas.estrategia))


    rodada = 1
    while len([j for j in jogadores if not j['morto']]) > 1:  # Enquanto mais de 1 jogador estiver vivo
        
        # Parte do código para imprimir o estado do jogo a cada 100 rodadas
        time.sleep(0.1)
        if rodada % 100 == 0:
            print(f"\n\n--- Rodada {rodada} ---\n")
            # Imprimir o estado atual dos jogadores que ainda estão vivos

            jogadores = sorted(jogadores, key=lambda x: x['vida'], reverse=True) # ordena a lista de jogadores (key='HP')
            for jogador in jogadores:
                if not jogador['morto']:
                    # print nome e vida do jogador, alinhado à direita, em ordem decrescente de vida assim como ataque atual do jogador
                    print(f"{jogador['nome']}: {jogador['vida']} HP | A: {jogador['bonus_ataque']}".rjust(35))

            # Ataque de dano aleatório a um alvo aleatório
            cerco(jogadores, rodada)

        # Para cada jogador, realizar uma ação (defender ou atacar)
        for jogador in jogadores: 
            rank = jogadores.index(jogador) # Índice do jogador na lista de jogadores
            realizar_acao(jogador, jogadores, rodada, rank) # Realiza a ação do jogador
        
        rodada += 1

    # Determinar o vencedor
    vencedor = [j for j in jogadores if not j['morto']][0] # Pega a lista de jogadores que não estão mortos (cujo tamanho é 1) e pega o idx=0
    print(f"\n{vencedor['nome']} venceu o jogo com {vencedor['vida']} HP na rodada {rodada}")


# Executar o jogo
if __name__ == "__main__": # Linha de execução principal
    jogo()



### --- Outras possíveis funcionalidades para implementar --- ###

# 1. Função que imprime o estado do jogo a cada N rodadas em ordem decrescente de vida (se possível, sem utilizar a função sort)
# 2. Atributo de bonus de ataque a cada vez que o jogador mata outro jogador (+10% de dano)
# 3. Estratégia de ataque arriscado, ou seja, há uma chance do ataque falhar ou então atacar todos os outros jogadores (Pr=0.20 de acertar)
# 4. Função de cura, que aumenta a vida do jogador em (inteiro aleatório entre +1 e +2)
# 5. Jogador recebe como parâmetro também o ranking dele em relação aos outros jogadores (no aspecto de vida)