from copy_book import start
import mouse
import keyboard as key
import pyautogui

ina = input("책 페이지 수를 적어주세요:")
while(True) :
    if key.is_pressed("s"):
        pos = mouse.get_position()
        break
print("지정완료!",pos,ina)
start(pos, ina)

    

    