import pyautogui
import time
from make_pdf_book import pngtopdf
from make_pdf_book import countp
def start(pos,cnt):
    pyautogui.moveTo(pos[0],pos[1],0.2)
    pyautogui.click()
    for i in range(int(cnt)): 
        pyautogui.hotkey("shift","s")
        time.sleep(0.7)
        pyautogui.click()
        pyautogui.scroll(-10)
        time.sleep(0.5)
        # pyautogui.screenshot(f'{path}img{i}.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
    pngtopdf(countp(cnt))
    
