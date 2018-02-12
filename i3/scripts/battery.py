#!/usr/bin/python3

import subprocess
import sys

class bcolors:    
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


result = subprocess.run(["acpi","-b","|","grep","\'Battery 0\'"], stdout=subprocess.PIPE)
result = result.stdout.decode('utf-8')

splited = result.split(" ")

status = splited[2][:-1]
percentage = int(splited[3][:-2])
control = False

if status == 'Discharging':
  output = ' DIS'
  control = True
else:
  output = ' CHR'

color = ""
if control:
    if percentage < 15:
        color = bcolors.RED
    elif percentage < 50:
        color = bcolors.YELLOW
    elif percentage < 80:
        color = bcolors.GREEN


print(splited[3][:-1]+output+"("+splited[4][:-3]+")"+"#B3000A\n")
#print("Hello")

