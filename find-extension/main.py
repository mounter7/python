import os

path = './test'

result = open('result.txt', 'w')

for x in os.listdir(path):
    result.write(x + '\n')

'''
for x in os.listdir('./test'):
    if x.endswith(ext):
        print(x)
'''