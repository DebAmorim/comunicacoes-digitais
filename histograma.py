import numpy as np


################################################################################
# Cálculo dos valores para construção de um histograma
################################################################################


def calcula_amplitude(array):
    array.sort()
    amplitude = array[len(array)-1] - array[0]
    return amplitude


def calcula_quantidade_classes(array):
    numero_classes = round(1+3.3*np.log(len(array)))
    return numero_classes


def calcula_amplitude_classe(array):
    ampliture_classe = round(calcula_amplitude(array)/calcula_quantidade_classes(array), 2)
    return ampliture_classe

