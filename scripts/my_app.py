from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

filmes = []

with open('../data/filmes_famosos.csv', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:
        dados = linha.strip().split(',')
        filme = {
            'id': int(dados[0]),
            'titulo': dados[1],
            'duracao': int(dados[2]),
            'genero': dados[3],
            'sinopse': dados[4],
            'nota': float(dados[5])
        }
        filmes.append(filme)


@app.route('/') # rota Home
def home():
    return render_template('home.html')

@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(filmes)

@app.route('/filmes/<int:id>', methods=['GET'])
def buscar_filme_por_id(id):
    for filme in filmes:
        if filme['id'] == id:
            return jsonify(filme)

@app.route('/filmes/busca', methods=['GET'])
def buscar_filme_por_nome():
    titulo = request.args['nome']

    if not titulo:
        return jsonify({'erro': 'Informe o parâmetro nome'})

    for filme in filmes:
        if filme['titulo'].lower() == titulo.lower():
            return jsonify(filme)


@app.route('/filmes', methods=['POST'])
def criar_filme():
    novo_filme = request.get_json()

    if not novo_filme:
        return jsonify({'erro': 'Nenhum dado enviado'})

    campos_obrigatorios = ['titulo', 'ano', 'genero']

    for campo in campos_obrigatorios:
        if campo not in novo_filme:
            return jsonify({'erro': f'O campo {campo} é obrigatório'})


    novo_id = max([filme['id'] for filme in filmes]) + 1

    filme = {
        'id': novo_id,
        'titulo': novo_filme['titulo'],
        'ano': novo_filme['ano'],
        'genero': novo_filme['genero']        
    }

    filmes.append(filme)

    return jsonify({
        'mensagem': 'Filme criado com sucesso',
        'filme': filme
    })


@app.route('/filmes/<int:id>', methods = ['PUT'])
def atualizar_filme_completo(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Nenhum dado enviado'})

    campos_obrigatorios = ['titulo', 'ano', 'genero']

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({'erro': f'O campo {campo} é obrigatório'})
        
    for filme in filmes:
        if filme['id'] == id:
            filme['titulo'] = dados['titulo']
            filme['ano'] = dados['ano']
            filme['genero'] = dados['genero']

            return jsonify({
                    'mensagem': 'Filme atualizado com sucesso',
                    'filme': filme
                })


@app.route('/filmes/<int:id>', methods = ['PATCH'])
def atualizar_filme_parcial(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Nenhum dado enviado'})
    
    for filme in filmes:
        if filme['id'] == id:
            
            if 'titulo' in dados:
                filme['titulo'] = dados['titulo']
            
            if 'ano' in dados:
                filme['ano'] = dados['ano']
            
            if 'genero' in dados:
                filme['genero'] = dados['genero']

            return jsonify({
                    'mensagem': 'Filme atualizado com sucesso',
                    'filme': filme
                })
        
@app.route('/filmes/<int:id>', methods=['DELETE'])
def deletar_filme(id):
    for filme in filmes:
        if filme['id'] == id:
            filmes.remove(filme)

            return jsonify({
                    'mensagem': 'Filme removido com sucesso',
                    'filme_removido': filme
                })

    return jsonify({'erro': 'Filme não encontrado'})


from threading import Thread
def rodar_servidor():
    app.run(debug=False, port=5000, use_reloader=False)

servidor = Thread(target=rodar_servidor)
servidor.start()