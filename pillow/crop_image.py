from PIL import Image
dog = Image.open("dog.jpg")

cropped = dog.crop((50, 100, 200, 350))
cropped.show()