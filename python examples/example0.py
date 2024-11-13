# Charger et afficher les données EMG

import pandas as pd
import matplotlib.pyplot as plt


file_path = 'emg_data.csv'
data = pd.read_csv(file_path)

# Afficher les 5 premières lignes du fichier pour vérifier
print(data.head())

# Tracer les données EMG
plt.plot(data['Time'], data['EMG'])
plt.title('Signal EMG')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (uV)')
plt.show()
