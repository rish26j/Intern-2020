from zipfile import ZipFile
import os


def file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


try:
    directory = input()
    file_paths2 = file_paths(directory)

    print("The files are")
    for file in file_paths2:
        print(file)

except:
    print((sys.exc_info()[0]), "occurred")
else:
    print("Files printed successfully")