from db.adapter import Database


def atualiza_perfil(nome, email, senha, dt_nasc, cep, token):
    db = Database()
    data = dt_nasc.split('/')
    dt_nasc = data[2] + '-' + data[1] + '-' + data[0]
    if len(senha) != 0:
        query = "UPDATE USUARIO " \
                "SET NOME = '{0}', EMAIL = '{1}', SENHA = '{2}', DTNASC = '{3}', CEP = '{4}' " \
                "WHERE TOKEN = '{5}'".format(nome, email, senha, dt_nasc, cep, token)
    else:
        query = "UPDATE USUARIO " \
                "SET NOME = '{0}', EMAIL = '{1}', DTNASC = '{2}', CEP = '{3}' " \
                "WHERE TOKEN = '{4}'".format(nome, email, dt_nasc, cep, token)

    try:
        db.execute(query)
        db.commit()
        return {"status": True}

    except:
        return {"status": False}


def get_perfil(token):
    db = Database()
    query = "SELECT NOME, EMAIL, cast(dtnasc as varchar(100)), CEP, DIAS, senha " \
            "FROM USUARIO " \
            "WHERE TOKEN = '{0}'".format(token)

    registros = db.select(query)
    registros = registros.pop()

    dtnasc = registros["dtnasc"].split("-")
    dtnasc = dtnasc[2] + '/' + dtnasc[1] + '/' + dtnasc[0]

    return {
        "nome": registros["nome"],
        "email": registros["email"],
        "dtnasc": dtnasc,
        "cep": registros["cep"],
        'dias': registros["dias"],
        'senha' : registros['senha']
    }