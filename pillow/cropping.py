from PIL import Image
import sys

try:
    federer = Image.open("federer.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)

cropped = federer.crop((100, 100, 350, 350))
cropped.save('federer_cropped.jpg')