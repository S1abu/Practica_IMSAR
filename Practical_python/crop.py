import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[100:200, 80:180]
cv2.imshow("Turtle face", cropped)
cv2.waitKey(0)