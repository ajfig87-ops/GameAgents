import subprocess
import time

class InputControl:
    def __init__(self):
        self.window_name = "Counter-Strike: Global Offensive"
    
    def focus_window(self):
        subprocess.run(["xdotool", "search", "--name", self.window_name, "windowactivate"], stderr=subprocess.DEVNULL)
    
    def move_mouse(self, dx, dy):
        self.focus_window()
        subprocess.run(["xdotool", "mousemove_relative", str(dx), str(dy)])
    
    def click(self, button="left"):
        self.focus_window()
        subprocess.run(["xdotool", "click", "1" if button == "left" else "3"])
    
    def hold_key(self, key, duration=0.1):
        self.focus_window()
        subprocess.run(["xdotool", "keydown", key])
        time.sleep(duration)
        subprocess.run(["xdotool", "keyup", key])
