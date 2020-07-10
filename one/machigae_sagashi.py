import cv2
import matplotlib.pyplot as pyplot
from PIL import Image

img1 = cv2.imread("gazou1.png")
img2 = cv2.imread("gazou2.png")

img_diff = cv2.absdiff(img1, img2)
img = Image.open("gazou1.png")
img_base = img.copy()
img_base.putalpha(128)
base = pyplot.imshow(img_diff)
pyplot.imshow(img_diff)
pyplot.imshow(img_base)
pyplot.show()




