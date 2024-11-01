import cv2 # type: ignore

img = cv2.imread('photo.jpg')
clahe = cv2.createCLAHE()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res = clahe.apply(gray_img)

cv2.imwrite('Enhanced_Photo.jpg', res)
print('Done enhancing')
