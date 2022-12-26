import pyautogui as mouse_controler
from pynput import keyboard, mouse
import time


# This is only for more advanced users skip this file if you dont know what you are doing
# This tool allows you to quickly save cordinats just take screenshot with your resolution open it on fullscreen and click on agents from left to righ LAST PICK IS LOCK BUTTON
time.sleep(1)

i = 0

cords = []
def get_pos(x, y, button, pressed):
    try:
        global i 
        if pressed:
            pos = mouse_controler.position()
            agents = ['Brimstone', 'Jett', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Sova', 'Astra', 'Breach', 'Chamber', 'Cypher', 'Fade', 'Harbor', 'KAY/O', 'Killjoy', 'Neon', 'Skye', 'Viper', 'Yoru', 'Lock']
            print(f'Position {pos.x} {pos.y} {agents[i]}')
            cords.append(agents[i]+':'+str(pos.x)+ 'x'+str(pos.y))

            i += 1
    except:
        print(cords)
mouse.Listener(on_click=get_pos).start()


while True:
    time.sleep(50)