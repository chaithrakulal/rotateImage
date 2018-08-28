import cv2
import numpy as np
img=cv2.imread("flower.jpg")
height, width = img.shape[:2]
rotate_mat = cv2.getRotationMatrix2D((width/2,height/2),70,0.7)
rotate_img = cv2.warpAffine(img,rotate_mat,(width,height))
cv2.imshow("rotated image",rotate_img)
cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
