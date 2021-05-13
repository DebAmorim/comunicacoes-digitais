import numpy as np
import matplotlib.pyplot as plt

quantidade_simbolos = 10000
n_bits_quantizador = 8
intervalos_l = 2**n_bits_quantizador
amplitude_sinal = 10
tamanho_delta = (2*amplitude_sinal)/intervalos_l

intervalo = np.linspace(0, 5, quantidade_simbolos)
onda_senoidal = np.sin(2*np.pi*1*intervalo)*amplitude_sinal


def niveis_de_quantizacao(sinal, amplitude_sinal):
    intervalo_decisao = []
    i = 0
    while i <= intervalos_l:
        intervalo_decisao.append(-amplitude_sinal+(tamanho_delta*i))
        i += 1
    print(intervalo_decisao)
    sinal_quantizado = []

    for amostra in sinal:
        j = 0
        while j < len(intervalo_decisao):
            if intervalo_decisao[j] <= amostra < intervalo_decisao[j+1]:
                sinal_quantizado.append(intervalo_decisao[j]+(tamanho_delta/2))
            j += 1
    print(sinal)
    print(sinal_quantizado)
    return sinal_quantizado


sinal_quantizado = niveis_de_quantizacao(onda_senoidal, amplitude_sinal)

if len(sinal_quantizado) > len(intervalo):
    sinal_quantizado.pop(len(sinal_quantizado)-1)

plt.plot(intervalo, sinal_quantizado, color='#142459')
plt.plot(intervalo, onda_senoidal, color='#db4cb2')
plt.title("Sinal Quantizado | " + str(intervalos_l) + " Níveis")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

