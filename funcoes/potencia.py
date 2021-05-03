import numpy as np


def calcula_snr(sinal, ruido):
    rms_sinal = 0
    rms_ruido = 0
    snr = 0
    snr_db = 0
    for amostra in sinal:
        rms_sinal += amostra**2
    for amostra in ruido:
        rms_ruido += amostra**2
    amplitude_sinal = np.sqrt(rms_sinal/len(sinal))
    amplitude_ruido = np.sqrt(rms_ruido/len(ruido))
    snr = (amplitude_sinal/amplitude_ruido)**2
    snr_db = 10 * np.log10(snr**2)
    print("SNR: " + str(round(snr, 2)) + " | SNRdb: " + str(round(snr_db, 2)))
