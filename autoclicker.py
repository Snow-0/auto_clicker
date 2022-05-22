import pyautogui as py


class AutoClicker:
    def __init__(self, single_click=1, mouse_button=True, interval=0.25):
        self.click = single_click
        self.interval = interval  # in seconds format
        self.mouse_button = mouse_button  # True left click and false for right click

    def mouse_click(self, x_pos=None, y_pos=None):
        if self.mouse_button:
            py.click(x_pos, y_pos, self.click, self.interval)
        else:
            py.rightClick(x_pos, y_pos, self.click, self.interval)

