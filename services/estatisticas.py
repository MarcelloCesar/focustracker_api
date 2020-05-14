def  retornaEstatisticas(doenca):
    retorno = {}

    if doenca == '3':
        retorno = {
            "confirmados" : 99,
            "suspeitos" : 99,
            "descartados" : 99,
            "curados" : 99,
            "obitos" : 99,
        }

    elif doenca == '2':
        retorno = {
            "confirmados" : 11,
            "suspeitos" : 11,
            "descartados" : 11,
            "curados" : 11,
            "obitos" : 11,
        }

    elif doenca == '1':
        retorno = {
            "confirmados" : 26,
            "suspeitos" : 33,
            "descartados" : 208,
            "curados" : 0,
            "obitos" : 1,
        }

    return retorno
