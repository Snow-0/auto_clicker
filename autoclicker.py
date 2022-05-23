import pyautogui as py

py.FAILSAFE = True


class AutoClicker:
    def __init__(self, single_click=1, mouse_button="Left", interval=0.25):
        self.click = single_click
        self.interval = interval  # in seconds format
        if mouse_button == "Right":
            self.mouse_button = False  # True left click and false for right click
        self.mouse_button = True

    def mouse_click(self, x_pos=None, y_pos=None):
        if self.mouse_button:
            py.click(x_pos, y_pos, self.click, self.interval)
        else:
            py.rightClick(x_pos, y_pos, self.click, self.interval)
