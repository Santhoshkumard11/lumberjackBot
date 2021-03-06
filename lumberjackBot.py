import pyautogui
import time
from ctypes import windll
import threading 


class lumberjackBot():

    __author__ = "EnriqueMoran"

    def __init__(self, playX, playY, treeX, treeY, x, y):
        self.playX = playX
        self.playY = playY
        self.treeX = treeX
        self.treeY = treeY
        # Those attributes has been placed here in order to save calcs: 
        self.x = x    # Left side branch X location
        self.y = y + 5   # Left side branch Y location
        self.movement_buffer = ["right"]    # First movement


    def move(self):
        speed = 0.14
        if self.movement_buffer[0] == "left" and len(self.movement_buffer) == 2:
            pyautogui.typewrite(['left', 'left'], speed)
        elif self.movement_buffer[0]  == "right" and len(self.movement_buffer) == 2:
            pyautogui.typewrite(['right', 'right'], speed)
        self.movement_buffer = self.movement_buffer[1:]

    def get_color(self, rgb):
        r = rgb & 0xff
        g = (rgb >> 8) & 0xff
        b = (rgb >> 16) & 0xff
        return r,g,b

    def get_pixel(self, x, y):    # Modify class atribute
        screen = windll.user32.GetDC(0)
        rgb = windll.gdi32.GetPixel(screen, x, y)
        return self.get_color(rgb)

    def play(self):
        while True:
            pixel_color = self.get_pixel(self.x, self.y)
            if pixel_color == (161, 116, 56):
                self.movement_buffer.append("right")
                self.move()
            elif pixel_color == (211, 247, 255) or pixel_color == (241, 252, 255):
                self.movement_buffer.append("left")
                self.move()
            #print(pixel_color, self.x, self.y, self.movement_buffer)
            


if __name__ == "__main__":
    print("Running in 3 seconds, minimize this windows. To stop the program drag the mouse to the top-left corner of your screen.")
    time.sleep(3)
    playX, playY = pyautogui.locateCenterOnScreen('playButton.png')
    pyautogui.moveTo(playX, playY)
    pyautogui.click()   # Start the game by pressing play button
    time.sleep(0.5)     # Wait for screen refresh
    x, y = pyautogui.locateCenterOnScreen('branch.png')
    pyautogui.moveTo(x, y + 5)
    treeX, treeY = playX - 6, playY - 177 # Tree position
    time.sleep(0.3)
    print("Im playing... To stop me click on IDLE and press CTRL+F6.")
    lumberjack = lumberjackBot(playX, playY, treeX, treeY, x, y)
    lumberjack.play()   # Game start
