import numpy as np
from PIL import Image as img
import cv2
import time

framedata = open("./frames.txt", "w", encoding="utf-8")

class Screen:
    def __init__(self, width = 160, height = 60):
        self.width = width
        self.height = height
        self.fps = 33.25
        self.on = '▓'
        self.off = '·'

    def draw(self, arr):
        buffer = ""
        for row in arr:
            for col in row:
                if col < 128:
                    buffer += self.off
                else:
                    buffer += self.on
            buffer += '\n'
        
        print("\033[2J\033[H" + buffer)
        framedata.write(buffer + "%\n")
        #time.sleep(1/self.fps)

disp = Screen(128, 64)

cap = cv2.VideoCapture(r"./【東方】Bad Apple ＰＶ【影絵】.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

f = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break   # No more frames → end of video

    
    small = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (disp.width, disp.height)) 
    small = (small >= 128).astype(np.uint8) * 255
    disp.draw(small)
    
    print(f"frame: {f}")
    f += 1

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
