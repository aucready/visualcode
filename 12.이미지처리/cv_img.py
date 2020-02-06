import cv2
import requests
import numpy
from PIL import Image
# PIL = RGB   with : height
# opencv = BGR   height : with



pil_img = Image.open('bg_a.jpg')
opencv_image = numpy.array(pil_img)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR) 

cv2.imshow('b', opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows







# url = 'https://cdn.pixabay.com/photo/2020/01/29/18/23/eyes-4803234_1280.jpg'

# arr = numpy.asarray(bytearray(requests.get(url).content),dtype=numpy.uint8)
# img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

# cv2.imshow('a', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# img = cv2.imread('bg_a.jpg', cv2.IMREAD_COLOR)

# print(img.shape)


# print(type(img))


# cv2.imshow('BG_a', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


