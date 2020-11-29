#!/usr/bin/env python3

import os, glob
from PIL import Image

os.chdir('supplier-data/images/')
size = 600, 400

for file in glob.glob('*.tiff'):
   f, e = os.path.splitext(file)
   fl = f + '.jpeg'
   with Image.open(file) as im:
      im.convert("RGB").resize((size)).save(fl)

