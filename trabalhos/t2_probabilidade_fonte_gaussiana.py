import numpy as np
import math
import scipy.special as sp
import matplotlib.pyplot as plt
from funcoes.fdp import calcula_fdp
from funcoes.distribuicao_gaussiana import gera_distribuicao_gaussiana
from funcoes.histograma import calcula_amplitude, calcula_quantidade_classes


media = 0
sigma = 1

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


def executa(quantidade_simbolos, probabilidade_zero=0.5, max=3, min=-3):

    valores_aleatorios = gera_distribuicao_gaussiana(quantidade_simbolos)
    x = gera_intervalo_probabilidade(max, min, quantidade_simbolos)
    probabilidade_x = calcula_fdp(x, 0, 1)
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


    plota_curva(x, probabilidade_x, quantidade_simbolos, probabilidade_zero, limiar, limiar_aproximado, limiar_aproximado2)
    plota_histograma(valores_unicos, numero_ocorrencias, quantidade_simbolos, probabilidade_zero)


def plota_histograma(valores_unicos, numero_ocorrencias, quantidade_simbolos, probabilidade_zero):
    plt.bar(valores_unicos, numero_ocorrencias, 0.2, color='pink')
    plt.title('Gerando ' + str(quantidade_simbolos) + " símbolos com P(x)=" + str(probabilidade_zero))
    plt.xlabel("Valores")
    plt.ylabel("Contagem")
    plt.show()


def plota_curva(x, probabilidade_x, quantidade_simbolos, probabilidade_zero, limiar, limiar_aproximado, limiar_aproximado2):
    plt.plot(x, probabilidade_x)
    plt.title('Gerando ' + str(quantidade_simbolos) + " símbolos com P(x)=" + str(probabilidade_zero))
    plt.axvline(limiar, color='red', label='Ideal', linewidth=4)
    plt.axvline(limiar_aproximado, label='ERFC', color='cyan')
    plt.axvline(limiar_aproximado2, label='Q(x)', color='orange')
    plt.legend(loc='upper right')
    plt.xlabel("Valores")
    plt.ylabel("Contagem")
    plt.show()