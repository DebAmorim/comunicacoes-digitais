import numpy as np
import math


################################################################################
# Cálculo da probabilidade de uma distribuição gaussiana com média sezo e
# variância unitária
################################################################################


media = 0
sigma = 1


def calcula_probabilidade(x):
    probabilidade = (1.0 / (sigma * np.sqrt(2.0 * math.pi))) * np.exp(-0.5 * ((x - media) / sigma) ** 2)
    return probabilidade