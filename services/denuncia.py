from db.adapter import Database


def inclui_denuncia(cep, tipo, coordenadas, observacao):
    cep = cep.strip()
    tipo = int(tipo)
    if observacao == '':
        observacao = ' '

    if coordenadas == '':
        coordenadas = ' '

    db = Database()
    query_bairro = "SELECT * " \
                   "FROM BAIRRO " \
                   "WHERE BAIRRO.CEP_INICIAL <= '{0}' OR BAIRRO.CEP_FINAL >= '{0}'".format(cep)

    registros = db.select(query_bairro)
    registros = registros.pop()

    query_denuncia = "INSERT INTO DENUNCIA (TIPO, BAIRRO, OBSERVACAO, COORDENADA)" \
                     "VALUES ({0}, {1}, '{2}', '{3}')".format(tipo, registros["id"], observacao, coordenadas)

    if tipo == 1:
        doenca = 4
    elif tipo == 2:
        doenca = 2
    else:
        doenca = None

    if doenca is not None:
        query_caso = "INSERT INTO CASO (DOENCA, SUSPEITO, BAIRRO) " \
                     "VALUES ({0}, {1}, {2})".format(doenca, 1, registros["id"])

    try:
        db.execute(query_denuncia)
        if doenca is not None:
            db.execute(query_caso)
        db.commit()
        return {"status": True}

    except:
        return {"status": False}