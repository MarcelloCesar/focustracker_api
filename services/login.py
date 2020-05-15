import uuid
import datetime

from db.adapter import Database

def efetuaLogin(email, senha):
    #trata o email
    #email = email.lower()

    #Recupera o BD
    bd = Database()

    registros = bd.select("select * from usuario where usuario.email = '%s'" % email)
    if(len(registros) <= 0):
        return {"status": False}

    usuario = registros.pop()

    # verifica se a senha foi informada corretamente
    if usuario["SENHA"] != senha:
        return {"status": False}


    horarioAtual = datetime.datetime.now()
    horarioExpiration = horarioAtual + datetime.timedelta(hours=2)
    horarioExpiration = horarioExpiration.strftime("%Y-%m-%d %H:%M:%S")

    token = uuid.uuid4().hex

    # Salva o token do usuario
    bd.execute("UPDATE USUARIO SET TOKEN='%s', expiration='%s' WHERE EMAIL='%s'" % (token, horarioExpiration, email))
    bd.commit()

    return {"status": True, "token" : token, "expiration" : horarioExpiration}


def cadastro(nome, email, senha, dtNasc, cep):
    db = Database()

    try:
        db.execute(
            "INSERT INTO USUARIO (NOME, EMAIL, SENHA, DTNASC, CEP) " +
            "VALUES ('%s', '%s', '%s', '%s', '%s') " % (nome, email, senha, dtNasc, cep)
        )

        db.commit()

        return efetuaLogin(email, senha)

    except:
        return {"status": False}




