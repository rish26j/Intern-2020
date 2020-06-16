from PIL import Image
import sys

try:
    federer = Image.open("federer.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)

rotated = federer.rotate(90)
rotated.save('federer_rotated.jpg')