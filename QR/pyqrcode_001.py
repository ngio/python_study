""" pyqrcode
    https://pypi.org/project/PyQRCode/
    >> pip install pyqrcode
    
    pypng
    https://pypi.org/project/pypng/
    >> pip install pypng
    
    Pillow (PIL Fork)
    https://pillow.readthedocs.io/en/latest/installation.html
    >> pip install Pillow
    
    1.pip 를 업데이트 하고 설치 하는 것이 좋다. 
    2.Prompt는 "관리자로 실행" 해서 설치 하시오. 
    python.exe -m pip install --upgrade pip
    
    * 설치된 패키지 확인
    pip list -v
"""
import os
import sys
os.environ['JAVA_OPTS'] = 'Xmx4096M'

import pyqrcode
import png
from PIL import Image 

print(" os.getcwd() : ", os.getcwd())


prePath = "./Project/QR/"
file_name = prePath + "QRCode.png" 

link = input("URL을 입력하세요~ : ")
qr_code = pyqrcode.create(link)
qr_code.png( file_name, scale=5)

img_open = Image.open(file_name)
img_open.show()
