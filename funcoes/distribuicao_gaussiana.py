from random import gauss
import numpy as np


media = 0
sigma = 1


def gera_distribuicao_gaussiana(quantidade_simbolos):
    valores = [gauss(media, sigma) for i in range(0,quantidade_simbolos)]
    return valores


def gera_distribuicao_normal(quantidade_simbolos):
    valores = np.random.normal(0, 1, quantidade_simbolos)
    return valores