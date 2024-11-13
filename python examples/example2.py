# Calculer la RMS (Root Mean Square) du signal EMG

import numpy as np

# Fonction pour calculer la RMS du signal
def calculate_rms(signal):
    return np.sqrt(np.mean(signal**2))

# Calculer la RMS du signal EMG filtré
rms_value = calculate_rms(filtered_emg)
print(f"La valeur RMS du signal EMG est : {rms_value} uV")

