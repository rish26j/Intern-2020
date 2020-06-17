from PIL import Image

dog = Image.open("dog.jpg")

rotated = dog.rotate(180)
rotated.show()