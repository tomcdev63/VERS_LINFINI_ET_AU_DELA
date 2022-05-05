import time, os, re
from uuid import UUID
import subprocess

devices = os.popen('sudo blkid').readlines()

usbs = []
for u in devices:
    loc = [u.split(':')[0]]
    if '/dev/sd' not in loc[0]: 
          continue # skip 
    loc+=re.findall(r'"[^"]+"',u)
    columns = ['loc']+re.findall(r'\b(\w+)=',u)
    
    usbs.append(dict(zip(columns,loc)))

print(usbs[0]["PARTUUID"])

commande_sound = 'mpg123 "../data/viead.mp3"'
commande_sound_closed = "pkill mpg123"

process = os.popen(commande_sound)
time.sleep(10)
os.popen(commande_sound_closed)