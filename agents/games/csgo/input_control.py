import subprocess
import time

class InputControl:
    def move_mouse(self, dx, dy):
        subprocess.run(["xdotool", "mousemove_relative", str(dx), str(dy)])
    
    def click(self, button="left"):
        subprocess.run(["xdotool", "click", "1" if button == "left" else "3"])
    
    def press_key(self, key):
        subprocess.run(["xdotool", "key", key])
    
    def hold_key(self, key, duration=0.1):
        subprocess.run(["xdotool", "keydown", key])
        time.sleep(duration)
        subprocess.run(["xdotool", "keyup", key])
