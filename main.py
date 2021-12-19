import numpy as np
import cv2
from pyzbar.pyzbar import decode

#path = 'qr_code.png'
#img = cv2.imread(path)
##code = decode(img)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('myData.txt') as f:
    myDataList= f.read().splitlines()

while True:

    success, img = cap.read()

    for qrcode in decode(img):

        print(qrcode.data)
        data = qrcode.data.decode('utf-8')
        print(data)

        if data in myDataList:
            print('Authorised')
        else:
            print('Unauthoreised')

        pts= np.array([qrcode.polygon],np.int32)
        pts= pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)

    cv2.imshow('Result', img)
    cv2.waitKey(1)

