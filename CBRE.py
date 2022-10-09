import os

from PIL import Image
import pytesseract


ocr_path = r'c:\Program Files\tesseract-OCR\tesseract.exe'

image_path = r'training-strips/'

pytesseract.tesseract_cmd = ocr_path

for root, dirs, file_names in os.walk(image_path):
    for file_name in file_names:
        image_convert = Image.open(image_path + file_name)

        text = pytesseract.image_to_string(image_convert)

        print(text)


