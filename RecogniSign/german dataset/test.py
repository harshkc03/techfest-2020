import os

f = open("Full/gt.txt", 'r').readlines()

label = list()

for file in f:
    temp = file.strip().split(';')[-1]
    label.append(int(temp))

label = sorted(label)

for i in range(0, 43):
    print(str(i)+":  "+str(label.count(i)))
    