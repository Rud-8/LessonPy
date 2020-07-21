#!/bin/python3

import requests

with open('essai') as file:
    lines = file.readline()
    print (''.join(lines))

for i in file :
    try:
        req = requests.get (lines, url="https://ipinfo.io")
