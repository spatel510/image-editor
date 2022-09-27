from PIL import Image, ImageEnhance, ImageFilter

import os

path = "./images"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    