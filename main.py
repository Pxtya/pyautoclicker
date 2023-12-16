import pyautogui
import keyboard
import time

def click():
    x, y = pyautogui.position()
    pyautogui.click(x, y)

def message(text):
    print("\033[95m" + text + "\033[0m")
    
running = False

message("Press 'q' to start,")

while True:
    keyboard.wait('q')
    
    running = not running
    
    if running:
        message("Auto Clicker has started, press 'e' to stop.")
    
    while running:
        click()
        time.sleep(1)

        if keyboard.is_pressed('e'):
            running = False

    message("Auto Clicker has stopped.")
    message("Made by Pxtya")
