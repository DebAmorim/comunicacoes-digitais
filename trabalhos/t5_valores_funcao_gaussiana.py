from funcoes.distribuicao_gaussiana import gera_distribuicao_gaussiana
import matplotlib.pyplot as plt
from funcoes.fdp import calcula_fdp
import numpy as np


media_gaussiana = 0
desvio_padrao = 1
quantidade_simbolos = 100000
funcao_gaussiana = gera_distribuicao_gaussiana(quantidade_simbolos, media_gaussiana, desvio_padrao)
line_width = 2.5


def gaussiana_ordenada(gaussiana):
    funcao_gaussiana_sorted = []
    for valor in gaussiana:
        funcao_gaussiana_sorted.append(valor)
    funcao_gaussiana_sorted.sort()
    return funcao_gaussiana_sorted


funcao_gaussiana_sorted = gaussiana_ordenada(funcao_gaussiana)
funcao_gaussiana_sorted.sort()
max = funcao_gaussiana[len(funcao_gaussiana_sorted)-1]
min = funcao_gaussiana[0]


def gera_intervalo_probabilidade(max, min, quantidade_simbolos):
    x = np.linspace(min, max, quantidade_simbolos)
    return x


def calcula_media_gaussiana(gaussiana):
    total = 0
    for valor in gaussiana:
        total += valor
    media = total/len(gaussiana)
    return media


def calcula_variancia_gaussiana(gaussiana, media):
    variancia = 0
    for valor in gaussiana:
        variancia += (valor - media)**2
    variancia = variancia/len(gaussiana)
    desvio_padrao = np.sqrt(variancia)
    return desvio_padrao


x = gera_intervalo_probabilidade(3, -3, quantidade_simbolos)
probabilidade_x = calcula_fdp(x, 0, 1)
media_gaussiana_calculada = calcula_media_gaussiana(funcao_gaussiana)
desvio_calculado = calcula_variancia_gaussiana(funcao_gaussiana, media_gaussiana_calculada)
print("Min: "+ str(min))
print("Max: "+ str(max))


plt.plot(funcao_gaussiana)
plt.title("Função Gaussiana")
plt.axhline(media_gaussiana, linewidth=line_width, color='purple', label='Média esperada: ' + str(media_gaussiana))
plt.axhline(media_gaussiana_calculada, linewidth=line_width, color='cyan',  label='Média calculada: '+str(round(media_gaussiana_calculada,4)))
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("F(x)")
plt.show()


plt.plot(x, probabilidade_x)
plt.title("Média | F.D.P. Gaussiana")
plt.axvline(media_gaussiana, linewidth=line_width, color='purple', label='Média esperada: ' + str(media_gaussiana))
plt.axvline(media_gaussiana_calculada, linewidth=line_width, color='cyan', label='Média calculada: '+str(round(media_gaussiana_calculada,4)))
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()


plt.plot(x, probabilidade_x)
plt.title("Comparativo Desvio Padrão | F.D.P. Gaussiana")
plt.axvline(media_gaussiana+desvio_calculado, linewidth=line_width, color='purple', label='Desvio Calculado: |' + str(round(desvio_calculado, 4))+"|")
plt.axvline(media_gaussiana-desvio_calculado, linewidth=line_width, color='purple')
plt.axvline(media_gaussiana+desvio_padrao, linewidth=line_width, color='cyan', label='Desvio Esperado: '+str(desvio_padrao))
plt.axvline(media_gaussiana-desvio_padrao, linewidth=line_width, color='cyan')
plt.axvline(media_gaussiana, color='orange', label='Média Esperada: '+str(media_gaussiana))
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()


plt.plot(x, probabilidade_x)
plt.title("Desvio Padrão e Média Calculados | F.D.P. Gaussiana")
plt.axvline(media_gaussiana_calculada+desvio_calculado, color='purple', label='Desvio Calculado: |' + str(round(desvio_calculado,4))+"|")
plt.axvline(media_gaussiana_calculada-desvio_calculado, color='purple')
plt.axvline(media_gaussiana_calculada, color='orange', label='Média Calculada: '+str(round(media_gaussiana_calculada,4)))
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()


media_calculada = [0.2227, 0.0621, 0.0127, 0.0052, 0.0008]
x_grafico = [100, 1000, 10000, 50000, 100000]

plt.plot(x_grafico, media_calculada, 'o-', label='Q(x) (encontrada)', color='red')
plt.grid()
plt.title("Média Em Função da Quantidade de Amostras")
plt.xlabel("x")
plt.ylabel("Média")
plt.show()


sigma_calculada = [0.0502, 0.0122, 0.0126, 0.0027, 0.0014]
x_grafico = [100, 1000, 10000, 50000, 100000]

plt.plot(x_grafico, sigma_calculada, 'o-', label='Q(x) (encontrada)', color='blue')
plt.grid()
plt.title("Variação do Desvio Padrão por Quantidade de Amostras")
plt.xlabel("x")
plt.ylabel("Variação do Desvio Padrão")
plt.show()
