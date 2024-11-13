# Analyse spectrale du signal EMG

# L'analyse spectrale est une méthode utilisée pour décomposer un signal en ses différentes fréquences composantes. Elle permet de comprendre la distribution des fréquences et d’analyser comment elles évoluent dans le temps

# Pourquoi faire une analyse spectrale ?

# Les signaux dans le domaine temporel, comme les signaux EMG (électromyogrammes), peuvent être complexes et difficiles à analyser directement. Cependant, si l'on examine un signal sous forme de spectre de fréquence, on peut mieux comprendre ses caractéristiques en termes de variations à différentes fréquences. Cela permet de :

    # 1. Isoler des composantes particulières : En séparant les différentes fréquences, on peut isoler des composantes d’un signal qui sont associées à certains phénomènes.
    # 2. Filtrer des fréquences indésirables : L'analyse spectrale permet d'identifier et de supprimer le bruit ou les interférences à des fréquences spécifiques, ce qui est essentiel dans des applications comme le traitement du signal EMG.
    # 3. Caractériser les propriétés d’un signal : En observant les pics dans le spectre, on peut déduire des informations sur la source ou la nature du signal.
    
# Comment fonctionne l'analyse spectrale ?

# L'analyse spectrale fonctionne en transformant un signal du domaine temporel (qui est représenté par des variations dans le temps) au domaine fréquentiel (qui est représenté par des variations en fonction de la fréquence).

# Cette transformation est souvent réalisée à l'aide de la Transformée de Fourier, une méthode mathématique qui décompose un signal en une somme de sinusoïdes à différentes fréquences. Il existe plusieurs types de Transformée de Fourier, et la plus courante est la Transformée de Fourier discrète (DFT), dont la version la plus utilisée est la Fast Fourier Transform (FFT).


from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Calculer la FFT du signal
N = len(filtered_emg)  # Nombre de points
T = 1.0 / fs  # Intervalle de temps entre les échantillons
x = np.linspace(0.0, N*T, N, endpoint=False)  # Axes temporel
yf = fft(filtered_emg)  # FFT du signal EMG
xf = fftfreq(N, T)[:N//2]  # Fréquences associées à la FFT

# Tracer le spectre
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.title('Analyse spectrale du signal EMG')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
