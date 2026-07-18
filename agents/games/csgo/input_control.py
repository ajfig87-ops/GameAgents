import pydirectinput
import time

class InputControl:
    def __init__(self):
        pydirectinput.FAILSAFE = False
    
    def move_mouse(self, dx, dy):
        pydirectinput.moveRel(dx, dy)
    
    def click(self, button="left"):
        if button == "left":
            pydirectinput.leftClick()
        else:
            pydirectinput.rightClick()
    
    def hold_key(self, key, duration=0.1):
        pydirectinput.keyDown(key)
        time.sleep(duration)
        pydirectinput.keyUp(key)
