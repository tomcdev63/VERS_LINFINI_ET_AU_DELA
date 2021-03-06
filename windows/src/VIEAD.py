from tkinter import *
from gtts import gTTS
import playsound
import requests
import serial.tools.list_ports
import webbrowser
import os
import time

root = Tk()
root.geometry("450x250")
root.title("VERS L'INFINI ET AU DELA! - Celestron C9.25 Fastar")

if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "G:/TOMDEV/VERS_LINFINI_ET_AU_DELA/windows/data/buzz.ico")
else:
    root.wm_iconbitmap(bitmap = "G:/TOMDEV/VERS_LINFINI_ET_AU_DELA/windows/data/buzz.xbm")

bg = PhotoImage(file="G:/TOMDEV/VERS_LINFINI_ET_AU_DELA/windows/data/wallpaper.png")
my_label = Label(root, image=bg).pack()

Msg = StringVar()
Label(root,text ="Code postal du lieu d'observation actuelle :", font = 'arial 11 bold', bg ='white smoke').place(x=35,y=20)
COORDONNEES = StringVar(value="Coords : ")
VILLES = StringVar(value="Ville: ")
label_city = Label(root,textvariable =VILLES, font = 'arial 11 bold', bg ='white smoke').place(x=35,y=160)
label_coords = Label(root,textvariable =COORDONNEES, font = 'arial 11 bold', bg ='white smoke').place(x=35,y=200)
entry_field = Entry(root, textvariable = Msg ,width ='20')
entry_field.place(x=35,y=60)

celestron_connected = BooleanVar(value=False)

def task():
    ports = serial.tools.list_ports.comports()
    if celestron_connected.get() == False and ports != []:
        print("connection")
        playsound.playsound(r"G:\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\buzz.mp3")
        celestron_connected.set(True)
    elif celestron_connected.get() == True and ports == []:
        print("deconnection")
        celestron_connected.set(False)
    root.after(500, task)

def Text_to_speech():
    Message = entry_field.get()
    city, long, lat = get_coordonees(Message)
    lat = str(lat)
    long = str(long)
    VILLES.set("Ville : " + city)
    COORDONNEES.set("Longitude : " + long[0:4] + " - " + "Latitude : " + lat[0:5])
    
    try:
        speech = gTTS(text = f"Vous êtes actuellement dans la ville de {city}, sa longitude est de {long[0:4]} degrés et sa latitude est de {lat[0:5]} degrés", lang="fr")
        speech.save(r'G:\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\geocoor.mp3')
        playsound.playsound(r'G:\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\geocoor.mp3', block=True)
    except Exception as e:
        print(e)

def get_coordonees(code_postal):
    response = requests.get(f"https://api-adresse.data.gouv.fr/search/?q=postcode={code_postal}")
    resp_json_payload = response.json()
    CITY = resp_json_payload["features"][2]["properties"]["city"]
    GEO_COOR = resp_json_payload["features"][2]["geometry"]["coordinates"]
    return CITY, GEO_COOR[0], GEO_COOR[1] 

def get_infos():
    CHEMINSN = "C:\Program Files (x86)\Starry Night Celestron SE 8\starrynight.exe"
    CHEMINS = "C:\Program Files\Stellarium\stellarium.exe"
    webbrowser.open("https://www.stelvision.com/astro/a-voir-actuellement-dans-le-ciel/")
    webbrowser.open("https://laclefdesetoiles.com/tubes-optiques-seuls/115-tube-optique-schmidt-cassegrain-celestron-c925-fastar-losmandy-c91027.html#:~:text=Le%20tube%20optique%20Celestron%20C9,ciel%20profond%20à%20grand%20champ.")
    webbrowser.open("https://stellarium-web.org")
    webbrowser.open("https://www.lameteoagricole.net")
    try:
        os.popen(CHEMINSN)
        time.sleep(10)
        os.popen(CHEMINS)
    except Exception as e:
        print(e)


def Exit():
    playsound.playsound(r"G:\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\goodbye.mp3")
    root.destroy()

def Reset():
    Msg.set("")
    COORDONNEES.set("")

def Welcome():
    playsound.playsound("G:\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\welcome.mp3")

Button(root, text = "LOOK", font = 'arial 15 bold' , command = Text_to_speech ,width = '6', bg = 'Green').place(x=35,y=98)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '6' , command = Exit, bg = 'Red').place(x=135 , y = 98)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset, bg = 'Orange').place(x=235 , y = 98)
Button(root, font = 'arial 15 bold',text = 'INFOS', width = '6' , command = get_infos).place(x=335 , y = 98)

# Welcome()
root.after(500, task)
root.mainloop()