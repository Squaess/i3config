#!/usr/bin/python3

import subprocess

result = subprocess.run(["light","-G"], stdout=subprocess.PIPE)

result = result.stdout.decode('utf-8')
result = str(round(float(result)))
print(result+"%")
