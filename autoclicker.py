import pyautogui as py
import time
import keyboard

py.FAILSAFE = True


class AutoClicker:
    def __init__(self, repeat, mouse_button, interval, x_pos, y_pos):
        self.repeat = repeat  # number of times to click
        self.interval = interval  # in seconds format
        if mouse_button == "Right":
            self.mouse_button = False  # True left click and false for right click
        self.mouse_button = True
        self.x_pos = x_pos
        self.y_pos = y_pos

    def single_click(self):
        time.sleep(3)
        while self.repeat > 0:
            if self.mouse_button:
                py.click(x=self.x_pos, y=self.y_pos, interval=self.interval)
                time.sleep(0.01)
            if not self.mouse_button:
                py.rightClick(x=self.x_pos, y=self.y_pos, interval=self.interval)
                time.sleep(0.01)
            if keyboard.is_pressed("q"):
                break
            self.repeat -= 1

    def double_click(self):
        time.sleep(3)
        while self.repeat > 0:
            if self.mouse_button:
                py.doubleClick(x=self.x_pos, y=self.y_pos, interval=self.interval)
                time.sleep(0.01)
            if not self.mouse_button:
                py.doubleClick(x=self.x_pos, y=self.y_pos, interval=self.interval, button="Right")
                time.sleep(0.01)
            if keyboard.is_pressed("q"):
                break
            self.repeat -= 1

    def repeat_until_stop(self):
        time.sleep(3)
        while True:
            py.click(x=self.x_pos, y=self.y_pos, interval=self.interval)
            time.sleep(0.02)
            if keyboard.is_pressed("q"):
                break
