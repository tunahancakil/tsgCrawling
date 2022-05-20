import os
import pathlib
from pdf2image import convert_from_path

for path in pathlib.Path("pdfs").iterdir():
    if path.is_file():
        current_file = open(path, "r")
        images = convert_from_path(current_file.name)
        for i in range(len(images)):
            selectDir = os.getcwd()
            print(selectDir)
            images[i].save(current_file.name + '-' + str(i) +'.jpg', 'JPEG')
        current_file.close()