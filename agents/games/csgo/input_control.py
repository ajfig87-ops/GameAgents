from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

class InputControl:
    def __init__(self):
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
    
    def move_mouse(self, dx, dy):
        self.mouse.move(dx, dy)
    
    def click(self, button=Button.left):
        self.mouse.click(button)
    
    def press_key(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)
    
    def hold_key(self, key, duration=0.1):
        self.keyboard.press(key)
        time.sleep(duration)
        self.keyboard.release(key)
