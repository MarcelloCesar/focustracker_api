from db.adapter import Database

def atualiza_perfil(nome, email, senha, dt_nasc, cep, token):
    db = Database()

    query = "UPDATE USUARIO " \
            "SET NOME = {0}, EMAIL = {1}, SENHA = {2}, DTNASC = {3}, CEP = {4} " \
            "WHERE TOKEN = {5}".format(nome, email, senha, dt_nasc, cep, token)

    try:
        db.execute(query)
        db.commit()

        return {"status": True}

    except:
        return {"status": False}