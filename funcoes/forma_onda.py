

def gera_onda_triagular(array, amplitude_sinal):
    onda_triangular = []
    dente_serra = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
    for amostra in array:
        if amostra > 0:
            for value in dente_serra:
                onda_triangular.append(value*amplitude_sinal/2)
        if amostra <= 0:
            for value in dente_serra:
                onda_triangular.append(-value*amplitude_sinal/2)

    return onda_triangular
