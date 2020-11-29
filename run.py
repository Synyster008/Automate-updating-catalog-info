
#! /usr/bin/env python3

import os
import requests
import json

url = "http://localhost/fruits/"
info={}
for file in files:
    fl = open("D:\\sample\\" + file, 'r')
    keys = ['name:', 'weight:']
    i=0
    info.clear()
    f=fl.readlines()
    d=''
    for i in range(2,len(f)):
        d=d+f[i].strip().replace(u'\xa0',u'')
    info=['description']=d
    info['name']=f[0].strip()
    info['weight']=f[1].strip(' lbs\n')
    info['image_name']=file.replace('.txt', '.jpeg')
    response = requests.post(url, json=info)
    print(response.request.url)
    print(response.status_code)

