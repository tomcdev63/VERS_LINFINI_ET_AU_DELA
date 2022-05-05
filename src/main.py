import time, os, re

USB_TEST = "082b5a3d-dd9b-478e-8a7d-6c906466e6b3"

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

if usbs[0]["PARTUUID"] == USB_TEST:

    commande_sound = 'mpg123 "../data/viead.mp3"'
    commande_sound_closed = "pkill mpg123"

    process = os.popen(commande_sound)
    time.sleep(10)
    os.popen(commande_sound_closed)