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

sound_file = '"../data/viead.mp3"'

devices.

p = subprocess.Popen(['mpg123', # The program to launch
                      '-C',     # Commands can be sent
                      '-q',     # Be quiet
                      sound_file],
                      stdin=subprocess.PIPE, # Send commands here
                      stdout=None,   
                      stderr=None)