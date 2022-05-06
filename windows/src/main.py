from tkinter import *
from gtts import gTTS
import playsound
import requests
import serial.tools.list_ports
import webbrowser


root = Tk()
root.geometry("400x300") 
root.configure(bg='ghost white')
root.title("VIEAD - CelestronC9.25 fastar")

Label(root, text = "VERS L'INFINI ET AU DELA!", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="DataFlair", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Code Postal du lieu d'obeservation actuelle :", font = 'arial 11', bg ='white smoke').place(x=20,y=60)
COORDONNEES = StringVar(value="Coords: ")
label_coords = Label(root,textvariable =COORDONNEES, font = 'arial 15 bold', bg ='white smoke').place(x=50,y=200)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

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

def get_astres_remarquables():
    webbrowser.open("https://www.stelvision.com/astro/a-voir-actuellement-dans-le-ciel/")

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

def Welcome():
    playsound.playsound(r"G:\TAF\TOMDEV\VERS_LINFINI_ET_AU_DELA\windows\data\welcome.mp3")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)
Button(root, font = 'arial 15 bold',text = 'INFOS', width = '6' , command = get_astres_remarquables).place(x=275 , y = 140)

root.after(500, task)
root.mainloop()