import time, os, re

USB_TEST = '082b5a3d-dd9b-478e-8a7d-6c906466e6b3'
COMMANDE_SOUND = 'mpg123 "../data/viead.mp3"'
COMMANDE_SOUND_OFF = "pkill mpg123"

# Liste 
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
print("")
print(usbs[1]["PARTUUID"])

print(usbs[0]["PARTUUID"])
print(type(usbs[0]["PARTUUID"]))
print(type(USB_TEST))

if usbs[0]["PARTUUID"] == USB_TEST:

    process = os.popen(COMMANDE_SOUND)
    time.sleep(10)
    os.popen(COMMANDE_SOUND_OFF)

else:
    print(usbs[0]["PARTUUID"], usbs[0]["PARTUUID"] == USB_TEST)