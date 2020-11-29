
#!/usr/bin/env python3
import requests
import glob,os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
os.chdir('supplier-data/images/')

for f in glob.glob('*.jpeg'):
    with open(f, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

