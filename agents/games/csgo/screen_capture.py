import mss
import numpy as np
import cv2

class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()
        self.monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}  # Adjust to your resolution
    
    def capture(self):
        screenshot = self.sct.grab(self.monitor)
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
