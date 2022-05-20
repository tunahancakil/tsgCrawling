import builtins
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'


original_open = open
def bin_open(filename, mode='rb'):       # note, the default mode now opens in binary
    return original_open(filename, mode)
print("read")

img = Image.open('images/adres.pdf')

try:
    builtins.open = bin_open
    bts = pytesseract.image_to_string(img, lang="tur")
    print("exchange")
finally:
    builtins.open = original_open

f= open("texts/TSG Text.txt","w+")
print("write")
f.write(bts)
f.close()