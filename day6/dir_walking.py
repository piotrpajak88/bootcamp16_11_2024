import os

print(os.path.abspath("../main.py"))
# C:\Users\88iro\PycharmProjects\bootcamp16_11_2024\pythonProject2\main.py

for root, dirs,files in os.walk("../.."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)
            # pass

    if files:
        print("Files")
        for file_ in files:
            print(file_)
            # pass