#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python wrappers to generate QR codes or read QR code from a file.
Requires the packages pypng, pyqrcode and pyzbar.
"""
def qrEncoder(text, destination=''):
    from pyqrcode import QRCode
    import png
    myQR = QRCode(text)
    if destination=='':
        myQR.show()
    else:
        myQR.png(destination+'.png', scale=8)

def qrDecode(imageFile):        
    from pyzbar.pyzbar import decode
    from PIL import Image
    
    img = Image.open(imageFile)
    result = decode(img)
    for i in result:
        print(i.data.decode("utf-8"))
