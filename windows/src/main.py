from tkinter import *
from gtts import gTTS
import playsound
import requests
import serial.tools.list_ports
import webbrowser

root = Tk()
root.geometry("450x208")
root.iconbitmap('../data/buzz.ico')
# root.configure(bg='ghost white')
root.title("VERS L'INFINI ET AU DELA! - Celestron C9.25 Fastar")

bg = PhotoImage(file="G:/TAF/TOMDEV/VERS_LINFINI_ET_AU_DELA/windows/data/wallpaper.png")
my_label = Label(root, image=bg).pack()

Msg = StringVar()
Label(root,text ="Code Postal du lieu d'obeservation actuelle :", font = 'arial 11 bold', bg ='white smoke').place(x=35,y=20)
COORDONNEES = StringVar(value="Coords: ")
label_coords = Label(root,textvariable =COORDONNEES, font = 'arial 11 bold', bg ='white smoke').place(x=35,y=160)
entry_field = Entry(root, textvariable = Msg ,width ='20')
entry_field.place(x=35,y=60)

celestron_connected = BooleanVar(value=False)

def task():
    ports = serial.tools.list_ports.comports()
    if celestron_connected.get() == False and ports != []:
        print("connection")
        playsound.playsound(r"G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\buzz.mp3")
        celestron_connected.set(True)
    elif celestron_connected.get() == True and ports == []:
        print("deconnection")
        celestron_connected.set(False)
    root.after(500, task)

def Text_to_speech():
    Message = entry_field.get()
    COORDONNEES.set("Coords: " + str(get_coordonees(Message)))
    try:
        speech = gTTS(text = Message)
        speech.save(r'G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\src\DataFlair.mp3')
        playsound.playsound(r'G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\src\DataFlair.mp3')
    except Exception as e:
        print(e)

def get_coordonees(code_postal):
    response = requests.get(f"https://api-adresse.data.gouv.fr/search/?q=postcode={code_postal}")
    resp_json_payload = response.json()
    LATITUDE = resp_json_payload["features"][2]["geometry"]["coordinates"]
    return LATITUDE

def get_infos():
    webbrowser.open("https://www.stelvision.com/astro/a-voir-actuellement-dans-le-ciel/")
    webbrowser.open("https://laclefdesetoiles.com/tubes-optiques-seuls/115-tube-optique-schmidt-cassegrain-celestron-c925-fastar-losmandy-c91027.html#:~:text=Le%20tube%20optique%20Celestron%20C9,ciel%20profond%20à%20grand%20champ.")
    webbrowser.open("https://stellarium-web.org")
    webbrowser.open("https://www.lameteoagricole.net")

def Exit():
    playsound.playsound(r"G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\goodbye.mp3")
    root.destroy()


def Reset():
    Msg.set("")
    COORDONNEES.set("")

def Welcome():
    playsound.playsound(r"G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\welcome.mp3")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '6', bg = 'Green').place(x=35,y=98)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '6' , command = Exit, bg = 'Red').place(x=135 , y = 98)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset, bg = 'Orange').place(x=235 , y = 98)
Button(root, font = 'arial 15 bold',text = 'INFOS', width = '6' , command = get_infos).place(x=335 , y = 98)

Welcome()
root.after(500, task)
root.mainloop()