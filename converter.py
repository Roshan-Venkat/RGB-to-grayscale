import cv2
import os
import glob
flag = 0
path = 'C:\\Users\\Roshan\\PycharmProjects\\machine learning\\output\\gray images'
name = input("enter a name:").split(",")
converted = []
for i in range(0,len(name)):
    for img in glob.glob('C:\\Users\\Roshan\\PycharmProjects\\machine learning\\input\\*.*'):
        if name[i] in img:
            image = cv2.imread(img)
            append = str(name[i]) + '.jpg'
            converted.append(name[i])
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(path, append), gray_image)
