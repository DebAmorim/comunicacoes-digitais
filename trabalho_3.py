import numpy as np
import math
import scipy.special as sp
import matplotlib.pyplot as plt
from probabilidade_x import calcula_probabilidade
from distribuicao_gaussiana import gera_distribuicao_gaussiana
from histograma import calcula_amplitude, calcula_quantidade_classes
from fonte_binaria_gaussiana import gera_simbolos_binarios, gera_simbolos_binarios_ideal


media = 0
sigma = 1


def gera_intervalo_probabilidade(max, min, quantidade_simbolos):
    x = np.linspace(min, max, quantidade_simbolos)
    return x


def gera_classes_histograma(array):
    min = -(calcula_amplitude(array)/2)
    max = abs(min)
    intervalos = np.linspace(min, max, calcula_quantidade_classes(array))
    return intervalos


def ajusta_valores_aleatorios_para_classes(valores_aleatorios, intervalos):
    valores = []
    i = 0
    while i < len(intervalos)-1:
        ocorrencias = preenche_classes(intervalos[i], intervalos[i + 1], valores_aleatorios)
        if ocorrencias > 0:
            j = 0
            while j < ocorrencias:
                j += 1
                valores.append((intervalos[i] + intervalos[i + 1])/2)
        i += 1

    return valores


def gera_array_valores_unicos_por_classe(array):
    valores = []

    for x in array:
        if x not in valores:
            valores.append(x)
    return valores


def preenche_frequencias(array, valores_unicos):
    ocorrencias = []
    for x in valores_unicos:
        ocorrencias.append(array.count(x))
    return ocorrencias


def preenche_classes(min, max, valores_aleatorios):
    ocorrencias = 0
    for valor in valores_aleatorios:
        if min <= valor < max:
            ocorrencias += 1
    return ocorrencias


def calcula_limiar_aproximado(p, array):
    i = 0
    while i < len(array):
        q = 0.5 + 0.5 * sp.erf(array[i] / np.sqrt(2))
        if q >= p:
            return array[i]
        i += 1

    return array[i]


def calcula_limiar_ideal(x, probabilidade_x, probabilidade_informada):
    # probabilidade_x.sort()
    # print(probabilidade_x)
    p_total = probabilidade_x.sum()
    q_total = 0
    i = 0
    while i < len(x):
        q_total += probabilidade_x[i]
        if q_total/p_total >= probabilidade_informada:
            return x[i]
        i += 1


def calcula_limiar_aproximado2(p, array):
    i = 1
    while i < len(array):
        q = (1/array[i]*np.sqrt(2*np.pi))*(1-(0.7/array[i]**2))*(math.e**(-array[i]/2)**2)
        if q >= p:

            return array[i]
        i += 1
    x_point = (i * (array[len(array) - 1] - array[0])) / len(array) + array[0]
    return x_point


def executa(quantidade_simbolos, probabilidade_zero=0.2, max=3, min=-3):

    valores_aleatorios = gera_distribuicao_gaussiana(quantidade_simbolos)
    x = gera_intervalo_probabilidade(max, min, quantidade_simbolos)
    probabilidade_x = calcula_probabilidade(x)
    intervalos = gera_classes_histograma(valores_aleatorios)
    valores_parametrizados = ajusta_valores_aleatorios_para_classes(valores_aleatorios, intervalos)
    valores_unicos = gera_array_valores_unicos_por_classe(valores_parametrizados)
    numero_ocorrencias = preenche_frequencias(valores_parametrizados, valores_unicos )
    limiar = calcula_limiar_ideal(x, probabilidade_x, probabilidade_zero)
    limiar_aproximado = calcula_limiar_aproximado(probabilidade_zero, x)
    limiar_aproximado2 = calcula_limiar_aproximado2(probabilidade_zero, x)

    print('\n')
    gera_simbolos_binarios_ideal(valores_aleatorios, probabilidade_zero, 'ideal')
    gera_simbolos_binarios(valores_aleatorios, limiar_aproximado, 'aproximado')
    print('\n')

    # plt.bar(valores_unicos, numero_ocorrencias, 0.2, color='pink')
    plt.plot(x, probabilidade_x)
    plt.axvline(limiar, color='red', linewidth=4 )
    plt.axvline(limiar_aproximado, color='cyan')
    plt.axvline(limiar_aproximado2, color='orange')
    # plt.axvline(limiar_aproximado2, color='cyan')
    plt.xlabel("Valores")
    plt.ylabel("Contagem")
    plt.show()
