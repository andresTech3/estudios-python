from cv2 import namedWindow,VideoCapture,imshow,waitKey

namedWindow('camara')
cv = VideoCapture(0)

while True:
    next,frame = cv.read()
    imshow("camara",frame)
    if(waitKey(50) >= 0):
        break