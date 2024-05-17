import pyautogui
import pyscreenshot
import pyautogui
from pytesseract import pytesseract
from time import sleep

count = 1
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
sleep(5)
pyautogui.moveTo(946,259)
sleep(3)
pyautogui.click()
sleep(8)

while True:
    pic = pyscreenshot.grab(bbox=(465,278,538,635))
    sleep(1)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(pic)
    modules = open('modules.txt', 'a')
    modules.write(text)

    if count > 1:
        for i in range(13):
            pyautogui.press('down')
            sleep(1)
    else:
        for i in range(25):
            pyautogui.press('down')
            sleep(1)
        count+=1

    modules.close

# lines_seen = set()

# file = open('modules2.txt', 'w')
# for line in open('modules.txt', 'r'):
#     if line not in lines_seen:
#         file.write(line)
#         lines_seen.add(line)
# file.close()
