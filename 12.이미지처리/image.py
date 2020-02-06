from PIL import Image
import requests

url = 'https://cdn.pixabay.com/photo/2020/01/11/10/08/landscape-4757115_1280.jpg'

r = requests.get(url, stream=True)
img_a = Image.open(r.raw)

img_a.show()
img_a.save('bg_a.jpg')





# img = Image.open('/Users/aucready/Downloads/ref_img/a.jpg')

# print(img.size)

# img = img.rotate(90)

# img.save('a_conv.png')

# img.show()


