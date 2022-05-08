# VERS_LINFINI_ET_AU_DELA 🔭

![Screenshot](https://github.com/tomcdev63/VERS_LINFINI_ET_AU_DELA/blob/main/windows/data/celestron.png?raw=true)

<!-- PROJECT LOGO -->
<br />
<p align="center">

<!-- SOMMAIRE -->
## Sommaire 📋

* [Sources](#sources)
* [Contexte_du_projet](#contexte_du_projet)
* [Construit_avec](#Construit_avec)
* [Installation](#Installation)
* [Usage](#usage)
 
<!-- SOURCES -->
## Sources

* https://adresse.data.gouv.fr/api-doc/adresse
* https://betterprogramming.pub/how-to-run-a-python-script-on-insertion-of-a-usb-device-2e86d38dcdb

<!-- CONTEXTE DU PROJET -->
## Contexte_du_projet 

Lors de jolies soirées d'été il m'arrive de partir avec des amis admirer le ciel, à l'aide de mon Celestron 9.25 Fastar sur monture CGX GOTO.  
Ce petit programme a pour but, à l'aide d'une interface graphique, d'envoyer une requête sur le site "https://api-adresse.data.gouv.fr" afin d'extraire les coordonnées géographiques du lieu d'observation en question.  
Notamment grâce à la latitude je pourrais facilement calibrer mon télescope.  
En complément le module gTTs analyse le texte transmis (coordonnées géographiques), le converti sous format MP3 et le restitue via "VIEAD" :)  
De plus la solution "VIEAD" est capable de reconnaitre le branchement de la monture CGX via les PORTSCOM et de lancer l'action souhaitée...  
Ici la phrase culte de Toy Story : Vers l'infini et au-delà!


<!-- CONSTRUIT AVEC -->
## Construit_avec 

* [Anaconda](https://www.anaconda.com/)

<!-- INSTALLATION -->
## Installation

* Clone du repos

    ```sh
    git clone https://github.com/tomcdev63/VERS_LINFINI_ET_AU_DELA.git
    ```
    
<!-- USAGE -->
## Usage 
 
* ```https://github.com/tomcdev63/VERS_LINFINI_ET_AU_DELA/blob/main/windows/src/main.py``` - Script Windows
* ```https://github.com/tomcdev63/VERS_LINFINI_ET_AU_DELA/blob/main/linux/src/main.py``` - Script Linux

    ```sh
    python VIEAD.py
    ```
![Screenshot](https://raw.githubusercontent.com/tomcdev63/VERS_LINFINI_ET_AU_DELA/main/windows/data/buzz.jpg)





