import cv2
import matplotlib.pyplot as pyplot
from PIL import Image

img1 = cv2.imread("gazou1.png")
img2 = cv2.imread("gazou2.png")

# 間違えを取得
diff = cv2.absdiff(img1, img2)

img = Image.open("gazou1.png")
img = img.copy()
img.putalpha(128)

pyplot.imshow(diff)
pyplot.imshow(img)
pyplot.show()
