# import numpy as np
# from PIL import Image

# width=5
# height=4
# array=np.zeros ([height, width, 3], dtype=np.uint8)
# img=Image.fromarray(array)
# img.save('test.png')

# array1=np.zeros( [100,200,3], dtype=np.uint8)
# array1 [:, :100]=[255,128, 0] #orange color
# array1 [: , 100: ]=[0, 0,255] #blue color
# img=Image.fromarray(array1)
# img.save('test1.png')

# # get color of a pixel
# im=Image. open('test1.png')
# rgb_im=im.convert('RGB')
# r,g,b=rgb_im.getpixel((1,1))
# print(r,g,b)

import scipy.misc
from PIL import Image
import numpy as np
import random

img=scipy.misc.imread("map-01.png")
count_pun=0
count_in=0
count=0
while(count <= 100000):
    x = random.randint(0,2735)
    y = random.randint(0,2480)
    z = 0
    if(img[x][y][z] == 60):
        count_in = count_in+1
        count = count+1
    else:
        if(img[x][y][z] == 80):
            count_pun = count_pun+1
            count = count+1

area_pun = (count_pun/count_in)*3287263
print(area_pun)