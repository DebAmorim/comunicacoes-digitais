################################################################################
# CANAL SIMÉTRICO BINÁRIO
# Uma imagem é utilizada como mensagem binária, enviada através do canal. O canal
# adiciona ruído à mensagem. Ao recuperar a imagem temos uma noção mais visual
# do que ocorre quando o ruído interfere na mensagem.
################################################################################

from funcoes.forma_onda import gera_onda_triagular
from funcoes.distribuicao_gaussiana import gera_distribuicao_gaussiana, gera_distribuicao_normal
from funcoes.gera_fonte_binaria import gera_sinal_binario
from funcoes.fdp import calcula_fdp
from funcoes.plotagem import plota_curva_com_eixo_y_em_zero, gera_intervalo_plotagem, plota_amplitudes, plota_pontos
from funcoes.imagens import converte_imagem_pb_em_vetor_binario, converte_vetor_binario_em_imagem_pb


n_bits = 1
sigma_ruido = 1
amplitude_sinal = 2*4.4


#1 Leitura da imagem


sinal_binario = converte_imagem_pb_em_vetor_binario()

#2 Transformar em onda triangular

mensagem = gera_onda_triagular(sinal_binario, amplitude_sinal)

#3 Criar sinal de ruído

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


intervalo_plotagem = gera_intervalo_plotagem(sigma_ruido*5, -sigma_ruido*5, 1000)
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

converte_vetor_binario_em_imagem_pb(mensagem_recuperada, amplitude_sinal)

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
# plota_amplitudes(fdp_ruido, intervalo_plotagem, amplitude_mensagem, "F.D.P. AWGN | Sigma: "+ str(sigma_ruido))
# plota_curva_com_eixo_y_em_zero(mensagem, "Mensagem Original")
# plota_curva_com_eixo_y_em_zero(sinal_transmitido, "Sinal Transmitido")
# plota_curva_com_eixo_y_em_zero(mensagem_recuperada_triangular, "Mensagem Recuperada")
# plota_pontos(erros, intervalo_plotagem_erro, "Bits com erro")


