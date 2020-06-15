from db.adapter import Database


def query(tipo, bairro, doenca):
    query_db = ""
    if tipo == "cura":
        query_db = "INSERT INTO CASO (DOENCA, CURADO, BAIRRO) " \
                   "VALUES ({0}, 1, {1})".format(doenca, bairro)

    if tipo == "obito":
        query_db = "INSERT INTO CASO (DOENCA, OBITO, BAIRRO) " \
                   "VALUES ({0}, 1, {1})".format(doenca, bairro)

    if tipo == "descarta":
        query_db = "INSERT INTO CASO (DOENCA, DESCARTADO, BAIRRO) " \
                   "VALUES ({0}, 1, {1})".format(doenca, bairro)

    if tipo == "confirma":
        query_db = "INSERT INTO CASO (DOENCA, CONFIRMADO, BAIRRO) " \
                   "VALUES ({0}, 1, {1})".format(doenca, bairro)
    return query_db


def atualiza_denuncia(id_denuncia, tipo):
    db = Database()

    query_del_caso = "DELETE FROM CASO WHERE DENUNCIA = {0}".format(id_denuncia)
    query_denuncia = "DELETE FROM DENUNCIA WHERE ID = {0}".format(id_denuncia)
    registro = db.select("SELECT * FROM DENUNCIA WHERE ID = {0}".format(id_denuncia))
    registro = registro.pop()

    doenca = None
    if registro["TIPO"] == 1:
        doenca = 4
    elif registro["TIPO"] == 2:
        doenca = 2

    query_bairro = "SELECT * " \
                   "FROM BAIRRO " \
                   "WHERE BAIRRO.CEP_INICIAL <= '{0}' OR BAIRRO.CEP_FINAL >= '{0}'".format(registro["CEP"])
    bairro = db.select(query_bairro).pop()
    bairro = bairro["ID"]
    print(bairro, doenca)
    query_caso = query(tipo, bairro, doenca)
    print(query_caso)
    try:
        db.execute(query_del_caso)
        db.execute(query_denuncia)
        if doenca is not None:
            db.execute(query_caso)
        db.commit()
        print("comitou")
        return {"status": True}
    except:
        return {"status": False}