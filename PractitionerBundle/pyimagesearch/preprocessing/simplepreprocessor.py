# import the necessary packages
import cv2

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        # Store the target width, height, and interpolation
        # Method used when resizing
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        # Resize the image to a fixed size, ignoring the aspect
        # ratio
        return cv2.resize(image, (self.width, self.height),
                          interpolation=self.inter)