from db.adapter import Database


def query(tipo, bairro):
    if tipo == "cura":
        query_db = "INSERT INTO CASO (DOENCA, CURADO, BAIRRO) " \
                   "VALUES (2, 1, '{0}'".format(bairro)

    if tipo == "obito":
        query_db = "INSERT INTO CASO (DOENCA, OBITO, BAIRRO) " \
                   "VALUES (2, 1, '{0}'".format(bairro)

    if tipo == "":
        query_db = "INSERT INTO CASO (DOENCA, CURADO, BAIRRO) " \
                   "VALUES (2, 1, '{0}'".format(bairro)

    if tipo == "cura":
        query_db = "INSERT INTO CASO (DOENCA, CURADO, BAIRRO) " \
                   "VALUES (2, 1, '{0}'".format(bairro)
def atualiza_denuncia(id_denuncia, tipo):
    db = Database()

    query_caso = "DELETE FROM CASO WHERE DENUNCIA = {0}".format(id_denuncia)
    query_denuncia = "DELETE FROM DENUNCIA WHERE ID = {0}".format(id_denuncia)