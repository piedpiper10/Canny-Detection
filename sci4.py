import numpy as np
import matplotlib.pyplot as plt 
import cv2
from skimage.data import camera
from skimage.filters import roberts, sobel, scharr, prewitt


image = cv2.imread('IMG_8792.jpg',0)

 
edge_roberts = roberts(image)
edge_sobel = sobel(image)

fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                       figsize=(10, 4))

ax[0].imshow(edge_roberts, cmap=plt.cm.gray)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_sobel, cmap=plt.cm.gray)
ax[1].set_title('Sobel Edge Detection')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
