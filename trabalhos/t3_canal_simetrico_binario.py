################################################################################
# CANAL SIMÉTRICO BINÁRIO
# Uma mensagem binária, aleatória, é enviada através do canal. O canal adiciona
# ruído à mensagem. Uma das técnicas utilizadas para recuperar a mensagem
# é manipular a SNR para que tenhamos potência do sinal > potência do ruído.
# Esta implementação corresponde ao exemplo 8.16, Lathi, 4a Edição
################################################################################
import numpy

from funcoes.forma_onda import gera_onda_triagular
from funcoes.distribuicao_gaussiana import gera_distribuicao_gaussiana, gera_distribuicao_normal
from funcoes.gera_fonte_binaria import gera_sinal_binario
from funcoes.fdp import calcula_fdp
from funcoes.plotagem import plota_curva_com_eixo_y_em_zero, gera_intervalo_plotagem, plota_amplitudes, plota_pontos, plota_cartesiano
from funcoes.potencia import calcula_snr

n_bits = 100000
sigma_ruido = 1
amplitude_sinal = 6


# 1 Criar sinal aleatório binário à partir de gaussiana

sinal_aleatorio = gera_distribuicao_gaussiana(n_bits)

sinal_binario = gera_sinal_binario(sinal_aleatorio)

#2 Transformar em onda triangular

mensagem = gera_onda_triagular(sinal_aleatorio, amplitude_sinal)

#3 Criar sinal de ruído

def gera_analise_ruido(ruido):
    ruido_ordenado = []
    for valor in ruido:
        ruido_ordenado.append(valor)
    ruido_ordenado.sort()
    amplitude_ruido = ruido_ordenado[len(ruido_ordenado) - 1] - ruido_ordenado[0]
    print("Vpp ruído (" + str(amplitude_ruido) + ") De: " + str(ruido_ordenado[0]) + " a " + str(ruido_ordenado[len(ruido_ordenado)-1]))


def gera_analise_mensagem(mensagem):
    mensagem_ordenada = []
    for valor in mensagem:
        mensagem_ordenada.append(valor)
    mensagem_ordenada.sort()
    amplitude_mensagem = mensagem_ordenada[len(mensagem_ordenada) - 1] - mensagem_ordenada[0]
    print("Vpp mensagem (" + str(amplitude_mensagem) + ") De: " + str(mensagem_ordenada[0]) + " a " + str(
        mensagem_ordenada[len(mensagem_ordenada) - 1]))
    amplitude = [mensagem_ordenada[0], mensagem_ordenada[len(mensagem_ordenada) - 1]]
    return amplitude


intervalo_plotagem = gera_intervalo_plotagem(sigma_ruido*5, -sigma_ruido*5, 20000)
intervalo_mensagem = gera_intervalo_plotagem(0.0, 10.0, 200)
fdp_ruido = calcula_fdp(intervalo_plotagem, 0, sigma_ruido)
quantidade_amostras = len(mensagem)
ruido = gera_distribuicao_gaussiana(quantidade_amostras, 0, sigma_ruido)
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


# recuperar mensagem


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
calcula_snr(mensagem, ruido)

print("O total de erros foi: " + str(total_erros))
print("Q(x)="+str((amplitude_sinal/2)/sigma_ruido))
plota_amplitudes(fdp_ruido, intervalo_plotagem, amplitude_mensagem, "Sigma: "+ str(sigma_ruido) + " | Ap: " + str(amplitude_sinal/2))
# plota_cartesiano(numpy.flip(mensagem), intervalo_mensagem, "Mensagem")
# plota_cartesiano(sinal_transmitido, intervalo_mensagem, "Sinal Transmitido")
# plota_cartesiano(numpy.flip(mensagem_recuperada_triangular), intervalo_mensagem, "Mensagem Recuperada")
# plota_curva_com_eixo_y_em_zero(sinal_transmitido, "Sinal Transmitido")
# plota_curva_com_eixo_y_em_zero(mensagem_recuperada_triangular, "Mensagem Recuperada")
# plota_pontos(numpy.flip(erros), intervalo_plotagem_erro, "Bits com erro")


# def plota_grafico_amplitude_fixada():
#     probabilidade_real = [0.16001, 0.1053, 0.04812, 0.02352, 0.01313, 0.00639, 0.0012, 0.0004, 0.000002, 0]
#     probabilidade_esperada = [0.1587, 0.1056, 0.04746, 0.02275, 0.01321, 0.00621, 0.001223, 0.0004342, 0.00003167,
#                               0.0000002867]
#     x = [1, 1.25, 1.67, 2, 2.22, 2.5, 3.03, 3.33, 4, 5]
#
#     plt.plot(x, probabilidade_real, 'o-', label='Q(x) (encontrada)', color='red')
#     plt.plot(x, probabilidade_esperada, 'o-', label='Q(x) (esperada)', color='blue')
#     plt.grid()
#     plt.title("Probabilidade de Erro na Detecção por Limiar")
#     plt.axhline(0.1, color='orange', label='Pontos de interesse')
#     plt.axhline(0.01, color='orange')
#     plt.axhline(0.001, color='orange')
#     plt.axvline(6, color='white', label='X = Ap (sinal)/Sigma (n)')
#     plt.legend(loc='upper right')
#     plt.xlabel("x")
#     plt.xlim(0, 6)
#     plt.ylabel("Pe")
#     plt.show()
#
#     probabilidade_real = [0.16001, 0.11439, 0.08059, 0.05491, 0.03597, 0.02297, 0.01347, 0.00798, 0.00514, 0.00245,
#                           0.00145, ]
#     probabilidade_esperada = [0.1587, 0.1151, 0.08076, 0.0548, 0.03593, 0.02275, 0.0139, 0.008198, 0.004661, 0.002555,
#                               0.00135]
#     x = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
#
#     plt.axhline(0.1, color='orange', label='Pontos de interesse')
#     plt.axhline(0.01, color='orange')
#     plt.axhline(0.001, color='orange')
#     plt.plot(x, probabilidade_real, 'o-', label='Q(x) (encontrada)', color='red')
#     plt.plot(x, probabilidade_esperada, 'o-', label='Q(x) (esperada)', color='blue')
#     plt.grid()
#     plt.title("Probabilidade de Erro na Detecção por Limiar | Sigma fixado")
#     plt.axvline(3.5, color='white', label='X = Ap (sinal)/Sigma (n)')
#     plt.legend(loc='upper right')
#     plt.xlabel("x")
#     plt.xlim(0.5, 3.5)
#     plt.ylabel("Pe")
#     plt.show()

