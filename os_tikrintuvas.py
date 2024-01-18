import os

path = "C:\\Users\\woite\\OneDrive\\Desktop\\30days siuntas laiko sarasas.txt"


if os.path.exists(path):
    print("Location Exists")
    if os.path.isfile(path):
        print("this is a file")
        file_status = os.stat(path)
        print(f"File: {path}")
        print(f"  Size: {file_status.st_size} bytes")
        print(f"  Last Modification Date: {file_status.st_mtime}")
    elif os.path.isdir(path):
        print("This is a folder")
else:
    print("Location non existance")