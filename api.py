from flask import Flask, make_response, request
import json
app = Flask(__name__)

def retornoApi(retorno):
    resp = make_response(json.dumps(retorno))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers["Access-Control-Allow-Credentials"] = True
    resp.headers["Access-Control-Allow-Headers"] = "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return resp


def autenticaUsuario():
    return True


@app.route('/login', methods=["POST", "GET"])
def login():
    from services.login import efetuaLogin

    retorno = ""
    if request.method == "POST":
        args = request.get_json(force=True)
        retorno = efetuaLogin(args.get('email'), args.get('senha'))

    return retornoApi(retorno)


@app.route('/cadastro', methods=["POST"])
def cadastro():
    from services.login import cadastro
    args = request.get_json(force=True)
    retorno = cadastro(
        args.get('nome'),
        args.get('email'),
        args.get('senha'),
        args.get('dtNasc'),
        args.get('cep')
    )

    return retornoApi(retorno)


@app.route('/estatistica', methods=["GET"])
def estatisticas():
    from services.estatisticas import retornaEstatisticas

    if not autenticaUsuario():
        return

    retorno = retornaEstatisticas(request.args.get('doenca'))
    return retornoApi(retorno)


@app.route('/perfil', methods=["POST", "GET"])
def perfil():
    from services.perfil import atualiza_perfil, get_perfil
    retorno = " "
    if not autenticaUsuario():
        return

    if request.method == "POST":
        args = request.get_json(force=True)
        retorno = atualiza_perfil(
            args.get('nome'),
            args.get('email'),
            args.get('senha'),
            args.get('dtNasc'),
            args.get('cep'),
            args.get('token')
        )

    elif request.method == "GET":
        retorno = get_perfil(request.args.get('token'))

    return retornoApi(retorno)


@app.route('/denuncia', methods=["POST", "GET"])
def denuncia():
    from services.denuncia import inclui_denuncia, get_denuncia
    if not autenticaUsuario():
        return
    if request.method == "POST":
        args = request.get_json(force=True)
        retorno = inclui_denuncia(args.get('cep'), args.get('tipo'), args.get('coordenadas'), args.get('observacao'), args.get('imagem'))

    elif request.method == "GET":
        retorno = get_denuncia(request.args.get('id'))

    return retornoApi(retorno)


@app.route('/gerenciamento', methods=['POST'])
def gerencia():
    from services.gerenciamento import atualiza_denuncia
    if not autenticaUsuario():
        return
    args = request.get_json(force=True)
    retorno = atualiza_denuncia(args.get('id'), args.get('tipo'))
    return retornoApi(retorno)


if __name__ == '__main__':
    app.run(debug=True)
