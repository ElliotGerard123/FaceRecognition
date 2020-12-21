"""
Description : functions to use SIFT methods for face recognation.


Author : ROGIE Elliot & Burgues Gerard

Devellopment:
__20/12/2020 :  -implement created_octave
                -implement created_dog_pictures
                -implement find_localextrem_keypoints
                -implement isEXTREM
___by : Elliot ROGIE
"""
import cv2
import glob
import numpy as np


def created_octave(image, nbr_of_octaves, nbf_in_octaves, sigma_blur=1.6):
    """
    Input:
        -image : image from OpenCV in black and white
        -(int)nbr_of_octaves : the number of octave you want
        -(int)nbr_in_octaves : the number of picture in an octave
    Output:
        -(int[][image]) octave : a list of octaves with for each octave the picture inside
        
    Description : created the octave pyraming image with using the function GaussianBlur from Opencv.
    
    """
    image = cv2.resize(image, (0, 0), fx=2, fy=2)
    octave =[]
    pictures_in_octave=[]
    #create the octave
    for i in range(nbr_octave):
        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        pictures_in_octave=[]
        pictures_in_octave.append(image)
        #image = cv2.resize(image, (int(image.shape[0] /2), int(image.shape[1] /2)))
        actual_picture=image
        for j in range(1,nbr_in_octave):
            picture_in_octave=cv2.GaussianBlur(actual_picture, (0,0), sigmaX=sigma_blur, sigmaY=sigma_blur)
            #explain it 
            pictures_in_octave.append(picture_in_octave)
            actual_picture=picture_in_octave
        octave.append(pictures_in_octave)
    return octave
    
def created_dog_pictures(octave, nbr_of_octaves, nbr_in_octave):
    """
    Input:
        -(int[][image]) octave : a list of octaves with for each octave the picture inside
        -(int)nbr_of_octaves : the number of octave you want
        -(int)nbr_in_octaves : the number of picture in an octave
    Output:
        -(int[][image]) dog : a list of dog with for each dog the picture inside
    Description: 
        -created dog(=Difference-of-Gaussians) image pyramid
    
    
    """
    dog=[]
    pictures_in_dog=[]
    for i in range(nbr_of_octaves):
        picture1=octave[i][0]
        picture2=octave[i][1]
        pictures_in_dog=[]
        pictures_in_dog.append(np.subtract(picture1, picture2))
        for j in range(2,nbr_in_octave):
            picture1=picture2
            picture2=octave[i][j]
            pictures_in_dog.append(np.subtract(picture1, picture2))
        dog.append(pictures_in_dog)
    return dog


def find_localextrem_keypoints(dog, nbr_of_octaves, nbr_in_octave):
    """
    Input:
        -(int[][image]) dog : a list of dog with for each dog the picture inside
        -(int)nbr_of_octaves : the number of octave you want
        -(int)nbr_in_octaves : the number of picture in an octave
        
    Output:
        -(int[][x,y]) Keypoints : the list of Keypoints for each picture tested
    
    Description : find locale extrem kp between the neirboord of the point and with the pixel of down and up pictures.
    
    """
    Keypoints=[]
    for i in range(nbr_of_octaves):
        for j in range(nbr_in_octave-3):
            first_picture=dot[i][j]
            middle_picture=dot[i][j+1]
            third_picture=dot[i][j+2]
            #print(first_picture)
            #print(first_picture.shape)
            kp_in_pictures=[]
            for u in range(2,first_picture.shape[0]-2):
                for v in range(2, first_picture.shape[1]-2):
                    if isEXTREM(first_picture[u-1:u+2, v-1:v+2], middle_picture[u-1:u+2, v-1:v+2], third_picture[u-1:u+2, v-1:v+2]):
                        kp_in_pictures.append([u,v])

            Keypoints.append(kp_in_pictures)
    return Keypoints

        
    
def isEXTREM(img1,img2,img3):
    """
    Input:
        -(image)img1 : the picture down (size 3*3)
        -(image)img2 : the picture tested(size 3*3)
        -(image)img3 : the picture up(size 3*3)
        
    Output: 
        -Boulean : if the point is local extrema
    
    """
    a=img2[1,1]
    for i in range(3):
        for j in range(3):
            if a<img1[i,j]:
                return False
            elif a<img2[i,j]:
                return False
            elif a<img3[i,j]:
                return False
    return True
        
        
        
        
