# EMG-Tutorial

# Tutoriel pour utiliser un capteur EMG avec OpenSignals

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- Un capteur EMG compatible avec OpenSignals (par exemple, un capteur de type MyoWare ou d'autres capteurs similaires).
- Le logiciel OpenSignals installé sur votre ordinateur.
- Un câble de connexion pour votre capteur EMG.
- Un ordinateur avec un port USB ou un autre port compatible pour la connexion du capteur.

## Étape 1 : Installation de OpenSignals

### 1.1 Télécharger OpenSignals

Rendez-vous sur le site officiel d'OpenSignals :  
[https://www.biopac.com/product/opensignals/](https://www.biopac.com/product/opensignals/)

Téléchargez la version compatible avec votre système d'exploitation (Windows, macOS, ou Linux).

### 1.2 Installer OpenSignals

Suivez les instructions d'installation pour votre système d'exploitation.

- **Windows :** Lancez le fichier `.exe` et suivez les instructions.
- **macOS :** Ouvrez le fichier `.dmg` et suivez les instructions.
- **Linux :** Téléchargez et installez le paquet approprié pour votre distribution.

### 1.3 Lancer OpenSignals

Une fois installé, lancez OpenSignals à partir du raccourci sur votre bureau ou dans votre menu de démarrage.

## Étape 2 : Connexion du capteur EMG à OpenSignals

### 2.1 Connecter le capteur EMG

Connectez votre capteur EMG à votre ordinateur via le câble approprié. Si votre capteur utilise un émetteur sans fil, assurez-vous qu'il est correctement appairé avec votre récepteur.

### 2.2 Configurer OpenSignals pour détecter le capteur

1. Ouvrez OpenSignals et allez dans le menu **Configuration**.
2. Sélectionnez **Périphériques** et choisissez le capteur EMG connecté.
3. Cliquez sur **OK** pour valider la configuration.

## Étape 3 : Collecte des données EMG

### 3.1 Créer un nouveau projet

1. Dans OpenSignals, cliquez sur **Nouveau Projet**.
2. Choisissez un nom pour votre projet et sélectionnez le capteur EMG dans la liste des appareils disponibles.
3. Cliquez sur **Démarrer l'enregistrement** pour commencer à collecter les données du capteur EMG.

### 3.2 Visualiser les signaux EMG

Pendant l'enregistrement, vous pouvez visualiser les signaux EMG en temps réel sur l'interface de OpenSignals. Utilisez les options de zoom et de mise à l'échelle pour mieux observer les détails du signal.

### 3.3 Ajuster les paramètres de collecte

Si nécessaire, ajustez les paramètres de collecte (fréquence d'échantillonnage, gain, etc.) pour obtenir des signaux plus clairs. Ces paramètres peuvent être modifiés dans le menu **Paramètres**.

## 3.4 : Suport visuel : 

![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/b8a98b20-a8ef-4f4c-b33a-356bb03b02cb)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/f0a7ef04-a7eb-4a81-8bbd-463712dd5d98)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/83e1a996-97d0-4042-a640-f85c4ab62091)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/07cc8092-41f1-409f-a40a-028f968b522a)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/b9e6d4b5-8c26-40a2-af35-db92ad90bf64)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/1ba4d883-8db8-44c2-bcbb-c6c4ada1f96c)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/6ad86e64-37a0-4065-bf4a-9c1e190720e7)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/f3d7cc0f-5ed6-40b6-a2d2-125711b59e9c)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/ef359856-07b8-4911-9e99-26ff529dc602)
![image](https://github.com/JulienQ1/EMG-Gamepad/assets/116632934/a15b4058-fbc8-4a73-861d-89d07092231d)

## Étape 4 : Analyser les données EMG

### 4.1 Exporter les données

Une fois que vous avez collecté suffisamment de données, vous pouvez les exporter pour une analyse plus approfondie :

1. Allez dans le menu **Fichier** et sélectionnez **Exporter les données**.
2. Choisissez le format de fichier souhaité (CSV, TXT, ou autre).
3. Sélectionnez l'emplacement de sauvegarde et cliquez sur **Enregistrer**.

### 4.2 Utiliser les outils d'analyse d'OpenSignals

OpenSignals propose des outils pour analyser les signaux EMG, tels que des filtres pour réduire le bruit ou des outils de détection d'événements pour identifier des contractions musculaires.

- **Filtres :** Appliquez des filtres passe-bas ou passe-haut pour nettoyer le signal.
- **Analyse spectrale :** Visualisez les composants fréquentiels du signal EMG.

### 4.3 Visualisation avancée

OpenSignals permet également de créer des graphiques et des rapports d'analyse en utilisant les données collectées. Explorez les fonctionnalités d'OpenSignals pour personnaliser vos graphiques et visualiser les résultats sous forme de courbes, histogrammes, etc.

## Étape 5 : Sauvegarde et partage des résultats

### 5.1 Sauvegarder le projet

1. Allez dans **Fichier** et sélectionnez **Sauvegarder le projet** pour conserver une copie de votre travail dans le format projet d'OpenSignals.
2. Vous pouvez également sauvegarder les résultats sous différents formats d'exportation pour une analyse ultérieure.

### 5.2 Partager les résultats

Si vous souhaitez partager vos résultats avec d'autres chercheurs ou collègues, vous pouvez exporter les données ou les graphiques dans un format compatible, comme PDF, CSV ou PNG.

## Conclusion

Vous avez maintenant une compréhension complète de la manière de configurer, collecter et analyser les données d'un capteur EMG avec OpenSignals. Cette procédure vous permettra de réaliser des études sur les signaux musculaires et de les exploiter pour des projets de recherche ou des applications biomédicales.

---

N'hésitez pas à adapter ce tutoriel en fonction de votre matériel spécifique et des fonctionnalités d'OpenSignals.