################################################################################
# Implementando canal simétrico binário e alterando valor de sigma do ruído
# para obter menor taxa de erro.
################################################################################
from funcoes.forma_onda import gera_onda_triagular
from funcoes.distribuicao_gaussiana import gera_distribuicao_gaussiana
from funcoes.gera_fonte_binaria import gera_sinal_binario
import matplotlib.pyplot as plt
import numpy as np
import math


n_bits = 100
sigma_ruido = 1
amplitude_sinal = 2


#1 Criar sinal aleatório binário à partir de gaussiana

sinal_aleatorio = gera_distribuicao_gaussiana(n_bits)

sinal_binario = gera_sinal_binario(sinal_aleatorio)

#2 Transformar em onda triangular

mensagem = gera_onda_triagular(sinal_aleatorio, amplitude_sinal)

def plota_curva_com_eixo_y_em_zero(mensagem, titulo):
    plt.plot(mensagem)
    plt.title(titulo)
    plt.axhline(0,  color='red')
    plt.xlabel("Valores")
    plt.ylabel("Contagem")
    plt.show()


#3 Criar sinal de ruído


def calcula_fdp_ruido(x):
    fdp = (1.0 / (sigma_ruido * np.sqrt(2.0 * math.pi))) * np.exp(-0.5 * ((x - 0) / sigma_ruido) ** 2)
    return fdp


def gera_ruido_gaussiano(quantidade_simbolos):
    ruido = np.random.normal(0, sigma_ruido, quantidade_simbolos)
    return ruido


def gera_analise_ruido(ruido):
    ruido_ordenado = []
    for valor in ruido:
        ruido_ordenado.append(valor)
    ruido_ordenado.sort()
    amplitude_ruido = ruido_ordenado[len(ruido_ordenado) - 1] - ruido_ordenado[0]
    print("Amplitude ruído (" + str(amplitude_ruido) + ") De: " + str(ruido_ordenado[0]) + " a " + str(ruido_ordenado[len(ruido_ordenado)-1]))


def gera_analise_mensagem(mensagem):
    mensagem_ordenada = []
    for valor in mensagem:
        mensagem_ordenada.append(valor)
    mensagem_ordenada.sort()
    amplitude_mensagem = mensagem_ordenada[len(mensagem_ordenada) - 1] - mensagem_ordenada[0]
    print("Amplitude mensagem (" + str(amplitude_mensagem) + ") De: " + str(mensagem_ordenada[0]) + " a " + str(
        mensagem_ordenada[len(mensagem_ordenada) - 1]))
    amplitude = [mensagem_ordenada[0], mensagem_ordenada[len(mensagem_ordenada) - 1]]
    return amplitude


def gera_intervalo_plotagem(max, min, quantidade_simbolos):
    x = np.linspace(min, max, quantidade_simbolos)
    return x



def plota_amplitudes(fdp_ruido, intervalo_plotagem, amplitude_mensagem, title):
    plt.plot(intervalo_plotagem, fdp_ruido)
    plt.title(title)
    plt.axvline(amplitude_mensagem[0], color='purple', label='-Ap')
    plt.axvline(amplitude_mensagem[1], label='+Ap', color='purple')
    # plt.axhline(0, color='orange')
    plt.legend(loc='upper right')
    plt.xlabel("n")
    plt.ylabel("P(n)")
    plt.show()


def plota_pontos(fdp_ruido, intervalo_plotagem, title):
    plt.plot(intervalo_plotagem, fdp_ruido, 'o')
    plt.title(title)
    # plt.axhline(0, color='orange')
    plt.xlabel("Bits")
    plt.ylabel("Diferença")
    plt.show()



intervalo_plotagem = gera_intervalo_plotagem(sigma_ruido*5, -sigma_ruido*5, 1000)
fdp_ruido = calcula_fdp_ruido(intervalo_plotagem)


quantidade_amostras = len(mensagem)
ruido = gera_ruido_gaussiano(quantidade_amostras)

amplitude_mensagem = gera_analise_mensagem(mensagem)
gera_analise_ruido(ruido)


# Adicionar ruído ao sinal


def gera_sinal_com_ruido(mensagem, ruido):
    sinal_transmitido = []
    i = 0
    while i < len(mensagem):
        sinal_transmitido.append(mensagem[i] + ruido[i])
        i += 1
    return sinal_transmitido


sinal_transmitido = gera_sinal_com_ruido(mensagem, ruido)



#recuperar mensagem


def recupera_mensagem(sinal_transmitido):
    mensagem_amostrada = []
    mensagem_original = []
    i = 0
    quantidade_amostras_valor_de_pico = round((len(sinal_transmitido)+1)/20)
    while i < quantidade_amostras_valor_de_pico:
        mensagem_amostrada.append(sinal_transmitido[(i*20) +10])
        i += 1

    for valor in mensagem_amostrada:
        if valor > 0:
            mensagem_original.append(1)
        else:
            mensagem_original.append(0)

    return mensagem_original


mensagem_recuperada = recupera_mensagem(sinal_transmitido)

def compara_mensagens_binarias(sinal_binario, mensagem_recuperada):
    i = 0
    mensagem_erro = []
    while i < len(sinal_binario):
        mensagem_erro.append(sinal_binario[i] - mensagem_recuperada[i])
        i += 1
    return mensagem_erro


def compara_mensagens(mensagem_original, mensagem_recuperada):
    print("Mensagem original: " + str(len(mensagem_original)))
    print("Mensagem recuperada: " + str(len(mensagem_recuperada)))
    i = 0
    erros = 0
    while i < len(mensagem_original):
        if mensagem_original[i] != mensagem_recuperada[i]:
            erros += 1
        i += 1

    return erros


erros = compara_mensagens_binarias(sinal_binario, mensagem_recuperada)
intervalo_plotagem_erro = gera_intervalo_plotagem(0, len(erros), len(erros))
mensagem_recuperada_triangular = gera_onda_triagular(mensagem_recuperada, amplitude_sinal)
total_erros = compara_mensagens(sinal_binario, mensagem_recuperada)


print("O total de erros foi: " + str(total_erros))
plota_amplitudes(fdp_ruido, intervalo_plotagem, amplitude_mensagem, "F.D.P. AWGN | Sigma: "+ str(sigma_ruido))
plota_curva_com_eixo_y_em_zero(mensagem, "Mensagem Original")
plota_curva_com_eixo_y_em_zero(sinal_transmitido, "Sinal Transmitido")
plota_curva_com_eixo_y_em_zero(mensagem_recuperada_triangular, "Mensagem Recuperada")
plota_pontos(erros, intervalo_plotagem_erro, "Bits com erro")


