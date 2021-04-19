

def gera_sinal_binario(sinal_aleatorio, limiar = 0):
    sinal_binario = []
    for amostra in sinal_aleatorio:
        if amostra < limiar:
            sinal_binario.append(0)
        else:
            sinal_binario.append(1)
    return sinal_binario