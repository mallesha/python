import os
path=input("Enter your path: ")

if os.path.exists(path):
    print(f'It is a valid path')

    if os.path.isfile(path):
        print(f'and the given path: {path} has a file')
    else:
        print(f'and the given path: {path} has a dirctory')
else:
    print(f'the path provided {path} is not a valid path in this system')
