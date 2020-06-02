from zipfile import ZipFile
file_name="city.zip"
with ZipFile(file_name,'r') as zip:
    print("Extracting all files........")

    zip.extract("jaipur.txt")
    zip.extractall()

    print("Files are extracted !")