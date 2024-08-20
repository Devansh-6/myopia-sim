import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


print(cv.__version__)
img  = cv.imread('./lorem-ipsum.jpg')

#2d convolution: replace central pixel in kernel with average of 25 pixels around it
kernel = np.ones((20,20), np.float32)/400
#creates 5x5 array of ones then divides it by 25
dst = cv.filter2D(img,-1,kernel)
#creates modified image with same depth, matrix is the previously created kernel

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging by 400')
plt.xticks([]),plt.yticks([])
plt.show()