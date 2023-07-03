import pyautogui
import pyscreenshot
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# position of the monster
pyautogui.moveTo(1470, 630)

while True:
    pic = ImageGrab.grab(bbox=(1424, 187, 1556, 240))
    text = pytesseract.image_to_string(pic)
    if "10/10" in text:
        pyautogui.moveTo(1544,74)
        pyautogui.click()

    pyautogui.moveTo(1470, 630)
    pyautogui.click()

