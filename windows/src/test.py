import serial.tools.list_ports
import playsound
import time
import os
import requests
import json



while True:
  ports = serial.tools.list_ports.comports()
  
  if ports != []:  
    # playsound.playsound(r"G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\buzz.mp3")
    # time.sleep(3)
    # playsound.playsound(r"G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\welcome.mp3")
    code_postal = input("Quel est le code postal du lieu de votre obeservation? ")
    response = requests.get(f"https://api-adresse.data.gouv.fr/search/?q=postcode={code_postal}")
    resp_json_payload = response.json()


    print(resp_json_payload)


  

    
    
    break

