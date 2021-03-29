

import numpy as numpy
import matplotlib.pyplot as plot

plot.close('all')

duracao_simbolos = 16
quantidade_simbolos = 60000
probabilidade = 0.5

aleatorio = numpy.random.rand(quantidade_simbolos)
aleatorio[numpy.where(aleatorio >= probabilidade)] = 1
aleatorio[numpy.where(aleatorio < probabilidade)] = 0

quantidadeZeros = 0
quantidadeUms = 0

for amostra in aleatorio:
    if amostra == 0:
        quantidadeZeros += 1
    else:
        quantidadeUms += 1


print("De um total de", quantidade_simbolos, "símbolos", quantidadeZeros, "foram 0 (Zero) e", quantidadeUms, "foram 1 (Um)")

 # gerando sinal

sinal = numpy.zeros(quantidade_simbolos*duracao_simbolos)
id_n = numpy.where(aleatorio == 1)

for i in id_n[0]:
    temp = int(i*duracao_simbolos)
    sinal[temp: temp+duracao_simbolos] = 1


plot.plot(sinal); plot.title('Fonte Binária Sem Memória Equiprovável')
plot.xlabel('Duração (seg)');plot.ylabel('Amplitude')
plot.show()