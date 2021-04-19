import numpy as np
import math


################################################################################
# Cálculo da função densidade de probabilidade de uma distribuição gaussiana
################################################################################


def calcula_fdp(x, media=0, sigma=1):
    probabilidade = (1.0 / (sigma * np.sqrt(2.0 * math.pi))) * np.exp(-0.5 * ((x - media) / sigma) ** 2)
    return probabilidade
