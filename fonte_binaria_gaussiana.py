import numpy as numpy
import matplotlib.pyplot as plot

################################################################################
# Modelagem de uma fonte binária, sem memória, a partir de uma
# distribuição gaussiana, com média 0 e variância 0.
################################################################################

def gera_simbolos_binarios(array, limiar, valor):
    i = 0
    sinal = []
    while i < len(array):
        if array[i] < limiar:
            sinal.append(0)
        else:
            sinal.append(1)
        i += 1
    gera_analise(sinal, valor)


def gera_simbolos_binarios_ideal(array, p, valor):
    i = 0
    sinal = []
    idx = round(len(array)*p)
    while i < len(array):
        if i < idx:
            sinal.append(0)
        else:
            sinal.append(1)
        i += 1
    gera_analise(sinal, valor)


def gera_analise(array, valor):
    quantidadeZeros = 0
    quantidadeUms = 0
    for amostra in array:
        if amostra == 0:
            quantidadeZeros += 1
        else:
            quantidadeUms += 1
    print("De um total de", len(array), "símbolos", round(quantidadeZeros / len(array) * 100, 2), "% foram 0 (Zero) e",
          round(quantidadeUms / len(array) * 100, 2), "% foram 1 (Um). O valor é " + str(valor) + ".")




