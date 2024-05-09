import pyautogui as pg
from pyautogui import *
import time
import pyperclip
import random as r


def drag_mouse(number_of_iterations):
    
    pg.sleep(1)
    pg.FAILSAFE = False

    for i in range(number_of_iterations):
        start_x, start_y = FindImagesOnScreen('Images/am.png', 'Images/pm.png')
        end_x, end_y = FindImagesOnScreen('Images/members.png')
        pg.moveTo(start_x, start_y, duration=1)
        pg.click(button='left')
        pg.sleep(1)
        pg.mouseDown(button='left')
        pg.moveTo(end_x, end_y, duration=1)
        time.sleep(3)
        pg.moveTo(end_x, end_y+60)
        time.sleep(1)
        pg.mouseUp(button='left')
        if text_paste_in_clipboard():
            read_and_write_text()
        
    
# for One Time Paste
def text_paste_in_clipboard():

    recent_value = ""
    while True:
        pyperclip.copy("")
        copy_text()
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            with open('clipboard.txt', 'a') as output:
                try:
                    output.write("%s\n\n" % str(tmp_value))
                    return True
                except:
                    continue
        else:
            return False
        
def FindImagesOnScreen(*ListOfImages):
    
    for image in ListOfImages:

        try:
            cordinate = pg.locateOnScreen(image, grayscale=True, confidence=0.8)
            return [cordinate[0], cordinate[1]+10] 
        except:
            pass
    try:
        cordinate = pg.locateOnScreen('Images/scroll.png', grayscale=True, confidence=0.99)
        return [cordinate[0]+20, cordinate[1]+20]
    except:
        raise Exception('Please open discord window')


def copy_text():
    pg.hotkey('ctrl', 'c', interval=0.3)

def read_and_write_text():
    with open('users.txt', 'a') as user:
        with open('clipboard.txt', 'r') as f:
            for line in f:
                line = line.split()
                try:
                    if line[-1] == 'PM' or line[-1] == 'AM':
                        user.write(str(line[0]) + '\n')
                except:
                    continue
                
if __name__ == '__main__':
    
    try:
        number_of_iterations = int(input('How many times you want to scroll: '))
    except:
        raise Exception('Please Enter Positive Number')
    pg.sleep(5)
    drag_mouse(number_of_iterations)