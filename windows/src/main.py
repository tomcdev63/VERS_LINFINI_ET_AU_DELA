import serial.tools.list_ports
import os

while True:
  ports = serial.tools.list_ports.comports()
  
  if ports != []:  
    os.popen("G:/TAF/TOMDEV/VERS_LINFINI_ET_AU_DELA/windows/data/viead.mp3")
    break