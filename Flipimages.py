###TRANSFORM pictures mirror efect
import numpy as np
import glob
import cv2
path  ="images/Gerard/*.*"

"""
i=0
for file in glob.glob(path):
    image = cv2.imread(file)
 
    image_show = cv2.flip(image, 1)
    cv2.imwrite("images/Gerard/Gerard_transform%i.jpeg"%i,image_show)
    cv2.imshow("image", image)
    cv2.imshow("image mirror",image_show)
    i+=1
"""

"""
for i in glob.glob(path):
    image = cv2.imread(i)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    """

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
