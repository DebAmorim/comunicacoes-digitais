import matplotlib.pyplot as plt
import numpy as np


def plota_curva_com_eixo_y_em_zero(mensagem, titulo):
    plt.plot(mensagem)
    plt.title(titulo)
    plt.axhline(0,  color='red')
    plt.xlabel("Valores")
    plt.ylabel("Contagem")
    plt.show()


def gera_intervalo_plotagem(max, min, quantidade_simbolos):
    x = np.linspace(min, max, quantidade_simbolos)
    return x


def plota_amplitudes(fdp_ruido, intervalo_plotagem, amplitude_mensagem, title):
    plt.plot(intervalo_plotagem, fdp_ruido)
    plt.title(title)
    plt.axvline(amplitude_mensagem[0], color='purple', label='-Ap')
    plt.axvline(amplitude_mensagem[1], label='+Ap', color='purple')
    plt.legend(loc='upper right')
    plt.xlabel("n")
    plt.ylabel("P(n)")
    plt.show()


def plota_pontos(fdp_ruido, intervalo_plotagem, title):
    plt.plot(intervalo_plotagem, fdp_ruido, 'o')
    plt.title(title)
    plt.xlabel("Bits")
    plt.ylabel("Diferença")
    plt.show()
