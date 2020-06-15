from db.adapter import Database


def monta_query(campo, doenca):
    query = "select count({0}) as casos from caso where doenca = {1} and {0} = 1".format(campo, doenca)
    return query.upper()


def retornaEstatisticas(doenca):
    bd = Database()
    retorno = {}

    query_conf = monta_query("confirmado", doenca)
    query_desc = monta_query("descartado", doenca)
    query_obito = monta_query("obito", doenca)
    query_curado = monta_query("curado", doenca)
    query_suspeito = monta_query("suspeito", doenca)

    confirmados = bd.select(query_conf)
    descartados = bd.select(query_desc)
    obitos = bd.select(query_obito)
    curados = bd.select(query_curado)
    suspeitos = bd.select(query_suspeito)

    retorno = {
        "confirmados": confirmados[0]["casos"],
        "suspeitos": suspeitos[0]["casos"],
        "descartados": descartados[0]["casos"],
        "curados": curados[0]["casos"],
        "obitos": obitos[0]["casos"]
    }

    return retorno
