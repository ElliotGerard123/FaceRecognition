import cv2
import glob
import numpy as np

face_cascade = cv2.CascadeClassifier('harcascade/haarcascade_frontalface_alt2.xml')
face_cascade_lateral = cv2.CascadeClassifier('harcascade/haarcascade_profileface.xml')
def ChangingContrast(image):
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 1.0  # Simple contrast control
    beta = 0  # Simple brightness control
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]): 
                new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)
    return new_image
def DetectFace(File):
    for file in glob.glob(File):

        file  = cv2.imread(file)
        #file = ChangingContrast(file1)
        file = cv2.resize(file, (500, 400) )
        face_gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(face_gray)
        faces_lateral = face_cascade_lateral.detectMultiScale(face_gray ,1.0485258, 6)

        #All pixels in face image

        if faces == () and faces_lateral == ():
            print("no face found")

        for (x1,y1,w1,h1) in faces_lateral:
            lateral = face_gray[y1:y1 + h1, x1:x1 + w1]
            color1 = (20, 20, 193 )  # BGR 0-255
            stroke1 = 2
            end_cord_x1 = x1 + w1
            end_cord_y1= y1 + h1
            frame1 = cv2.rectangle(face_gray, (x1, y1), (end_cord_x1, end_cord_y1), color1, stroke1)

        for (x,y,w,h) in faces:
            center = face_gray[y:y+ h, x:x+w]

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            frame = cv2.rectangle(face_gray, (x, y), (end_cord_x, end_cord_y), color, stroke)
            ## Here will do lateral face

        cv2.imshow('Capture - Face detection', face_gray)
        cv2.waitKey(0)




DetectFace("images/Gerard/*.*")


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)