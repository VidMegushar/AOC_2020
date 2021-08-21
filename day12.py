import math
import cv2
import imutils
import os
import numpy as np

image = cv2.imread("space.jpg")
rocket = cv2.imread("rocket1.png")

rocket = cv2.resize(rocket, (25, 25))
image = cv2.resize(image, (1900, 1000))



cv2.imshow('slika', image)
cv2.waitKey(0)

with open('input12.txt') as f:
    pos = [0,0]
    wayp = [10, 1]
    dirs = [[1,0], [0,-1], [-1,0], [0,1]]
    for line in f.readlines():
        prev_pos = [x for x in pos]
        d, val = line.strip()[0], int(line.strip()[1:])
        if d == "F":
            pos[0] += val*wayp[0]
            pos[1] += val*wayp[1]
        elif d == "N":
            wayp[1] += val
        elif d == "S":
            wayp[1] -= val
        elif d == "E":
            wayp[0] += val
        elif d == "W":
            wayp[0] -= val
        elif d == "R":
            sin = round(math.sin(math.radians(-val)))
            cos = round(math.cos(math.radians(-val)))
            wayp[0], wayp[1] = cos*wayp[0] - sin*wayp[1], sin*wayp[0] + cos*wayp[1]
        elif d == "L":
            sin = round(math.sin(math.radians(val)))
            cos = round(math.cos(math.radians(val)))
            wayp[0], wayp[1] = cos*wayp[0] - sin*wayp[1], sin*wayp[0] + cos*wayp[1]
        
        start_pos = (int(prev_pos[0]/50) + 1100, int(prev_pos[1]/50) + 500)
        end_pos = (int(pos[0]/50) + 1100, int(pos[1]/50) + 500)

        color = (32, 140, 186)
        cv2.line(image, start_pos, end_pos, color, 1)
        tmp_image = image.copy()
        tmp_image[end_pos[1]-10:end_pos[1]-10+rocket.shape[0], end_pos[0]-10:end_pos[0]-10+rocket.shape[1]] = rocket

        center_coordinates = (end_pos[0] + wayp[0], end_pos[1] + wayp[1])
        cv2.circle(tmp_image, center_coordinates, 3, color, 3)
        cv2.imshow('slika', tmp_image)
        cv2.waitKey(20)

cv2.imshow('slika', tmp_image)
cv2.waitKey(0)

print(abs(pos[0]) + abs(pos[1]))