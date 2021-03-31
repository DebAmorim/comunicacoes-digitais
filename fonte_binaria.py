

import numpy as numpy
import matplotlib.pyplot as plot

################################################################################
# Modelagem de uma fonte discreta sem memória
################################################################################

def gera_analise_simbolos(array):
    quantidadeZeros = 0
    quantidadeUms = 0
    for amostra in array:
        if amostra == 0:
            quantidadeZeros += 1
        else:
            quantidadeUms +=1
    print("De um total de", len(array), "símbolos", round(quantidadeZeros/len(array)*100,2), "% foram 0 (Zero) e", round(quantidadeUms/len(array)*100,2), "% foram 1 (Um)")


def plota_simbolos(array, quantidade_simbolos, duracao_simbolos):
    sinal = numpy.zeros(quantidade_simbolos * duracao_simbolos)
    sinalUm = numpy.where(array == 1)

    for i in sinalUm[0]:
        temp = int(i * duracao_simbolos)
        sinal[temp: temp + duracao_simbolos] = 1

    plot.plot(sinal);
    plot.title('Fonte Binária Sem Memória')
    plot.xlabel('Bits transmitidos');
    plot.ylabel('Amplitude')
    plot.show()


def gera_simbolos(quantidade_simbolos = 0, probabilidade_zero = 0, duracao_simbolos = 0):
    plot.close('all')

    aleatorio = numpy.random.rand(quantidade_simbolos)
    aleatorio[numpy.where(aleatorio >= probabilidade_zero)] = 1
    aleatorio[numpy.where(aleatorio < probabilidade_zero)] = 0
    gera_analise_simbolos(aleatorio)
    if duracao_simbolos > 0:
        plota_simbolos(aleatorio, quantidade_simbolos, duracao_simbolos)


