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

    retorno = efetuaLogin(request.args.get('email'), request.args.get('senha'))
    return retornoApi(retorno)


@app.route('/cadastro', methods=["POST"])
def cadastro():
    from services.login import cadastro

    print([x for x in request.args])
    retorno = cadastro(
        request.args.get('nome'),
        request.args.get('email'),
        request.args.get('senha'),
        request.args.get('dtNasc'),
        request.args.get('cep'),
    )

    return retornoApi(retorno)


@app.route('/estatistica', methods=["GET"])
def estatisticas():
    from services.estatisticas import retornaEstatisticas

    if not autenticaUsuario():
        return

    retorno = retornaEstatisticas(request.args.get('doenca'))
    return retornoApi(retorno)


@app.route('/perfil', methods=["POST"])
def perfil():
    from services.perfil import atualiza_perfil

    if not autenticaUsuario():
        return

    retorno = atualiza_perfil(
        request.args.get('nome'),
        request.args.get('email'),
        request.args.get('senha'),
        request.args.get('dtNasc'),
        request.args.get('cep'),
        request.args.get('token')
    )

    return retornoApi(retorno)
