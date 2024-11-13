#  Filtrage du signal EMG (Filtre passe-bande)

import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Fonction pour créer un filtre passe-bande
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

# Application du filtre sur les données
def bandpass_filter(data, lowcut, highcut, fs):
    b, a = butter_bandpass(lowcut, highcut, fs)
    return filtfilt(b, a, data)

# Paramètres du filtre
lowcut = 20.0  # Fréquence basse en Hz
highcut = 450.0  # Fréquence haute en Hz
fs = 1000  # Fréquence d'échantillonnage en Hz

# Appliquer le filtre aux données EMG (présumées être dans 'data['EMG']')
filtered_emg = bandpass_filter(data['EMG'], lowcut, highcut, fs)

# Tracer le signal filtré
plt.plot(data['Time'], filtered_emg)
plt.title('Signal EMG filtré')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (uV)')
plt.show()
