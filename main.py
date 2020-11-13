import pyautogui
import pytesseract
import time
import pygame
from pygame.locals import *



def Main():
    while (True):
        time.sleep(5)
        # Take Screenshot
        take_screenshot = pyautogui.screenshot()
        take_screenshot.save(r'H:\Personal_Python\ScreenShotText\capture.png')
        print("[INFO] Screenshot taken and saved")

        # Translate into stirng
        time.sleep(1)
        print("[INFO] Translating into string")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        str_in_image = pytesseract.image_to_string(r'H:\Personal_Python\ScreenShotText\capture.png')
        
        # Check for words
        if ("leo" in str(str_in_image.lower())):
            print("[FOUND] Word Found")
            pygame.mixer.init()
            print("[INFO] Loaded Sound")
            pygame.mixer.music.load('play.mp3')
            print("[INFO] Playing Sound")
            pygame.mixer.music.play(0)
            pass
        else:
            pass


Main()
