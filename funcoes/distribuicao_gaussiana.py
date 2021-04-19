from random import gauss
import numpy as np


def gera_distribuicao_gaussiana(quantidade_simbolos, media=0, sigma=1):
    valores = [gauss(media, sigma) for i in range(0, quantidade_simbolos)]
    return valores


def gera_distribuicao_normal(quantidade_simbolos, media=0, sigma=1):
    valores = np.random.normal(media, sigma, quantidade_simbolos)
    return valores