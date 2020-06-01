import os
import sys

path=input("Enetr your directory path:")

if os.path.exists(path):
    print("f{path} is a valid path")
else:
    print("f{path} is not a valid path")
    sys.exit()
list_of_dirNfiles=os.listdir(path)
print(list_of_dirNfiles)
for each_data in list_of_dirNfiles:
    drf=os.path.join(path, each_data)

    if os.path.isfile(drf):
        print(f'{drf} is a file')
    else:
        print(f'{drf} is a dir')



