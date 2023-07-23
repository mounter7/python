import os

currentPath = '.'

for item in os.listdir(currentPath):
    print(item)
    if not os.path.isfile(item):
        for file in os.listdir(item):
            if file.endswith('txt'):
                print(file)