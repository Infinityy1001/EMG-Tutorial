# Détecter des événements (contractions musculaires) à partir du signal EMG

import matplotlib.pyplot as plt
import numpy as np

# Import les data et les filtrer

# Définir un seuil pour la détection des contractions
threshold = 0.1  # seuil en uV (à ajuster selon vos données)

# Détecter les indices où le signal dépasse le seuil
contraction_indices = np.where(filtered_emg > threshold)[0]

# Afficher les résultats
print(f"Indices des contractions détectées : {contraction_indices}")

# Tracer le signal avec les contractions détectées
plt.plot(data['Time'], filtered_emg)
plt.scatter(data['Time'][contraction_indices], filtered_emg[contraction_indices], color='red')
plt.title('Détection des contractions musculaires')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (uV)')
plt.show()
