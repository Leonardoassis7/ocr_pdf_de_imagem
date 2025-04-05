#openbcv reconhecer imagem
#pytesseract #inteligencia de reconhecimento de caratcer
#Dica para teste futuro caso tenha erro tesseract baixa o installador ( https://github.com/UB-Mannheim/tesseract/wiki)
#grava onde instalou pq vai que apontar para lá exemplo C:
#smallpdf.com converte primeiro converti o pdf para uma imagem depois alterei para pdf novamente
#https://github.com/oschwartz10612/poppler-windows/releases coloquei na variavel de ambiente

import cv2 
import numpy as np
import pytesseract
from pdf2image import convert_from_path

#caminho do tessetact / poppler
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
poppler_path = "C:/Users/Leonardo Assis/Downloads/Poppler/poppler-24.08.0/Library/bin"

# Converte PDF em imagens usando o Poppler
paginas = convert_from_path('imagem.pdf', poppler_path=poppler_path)

for i, pagina in enumerate(paginas):
    imagem_cv = cv2.cvtColor(np.array(pagina), cv2.COLOR_RGB2BGR)
    imagem_cinza = cv2.cvtColor(imagem_cv, cv2.COLOR_BGR2GRAY)
    _, imagem_bin = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY)

    resultado = pytesseract.image_to_string(imagem_bin)
    print(f"Página {i+1}:\n{resultado}\n{'-'*40}")