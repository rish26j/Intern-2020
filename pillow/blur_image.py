from PIL import Image, ImageFilter
import sys

img = Image.open("dog.jpg")

blurred = img.filter(ImageFilter.BLUR)

blurred.show()