from zipfile import ZipFile

fname="city.zip"

with ZipFile(fname,'r') as zip:
    print("Extracting all files........")

    zip.extract("jaipur.txt")
    zip.extractall()

    print("Files are extracted !")
