import pyautogui as mouse_controler
from pynput import mouse
import time, os

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
        if not os.path.exists('theme/cords.txt'):
    
            with open('theme/cords.txt','a+')as cordsf:
                cordsf.write("ags = ['Brimstone:653x838', 'Jett:748x845', 'Omen:827x844', 'Phoenix:912x845', 'Raze:1003x843', 'Reyna:1081x847', 'Sage:1178x838', 'Sova:1248x845', 'Astra:643x925', 'Breach:760x924', 'Chamber:826x922', 'Cypher:917x924', 'Fade:998x926', 'Harbor:1086x937', 'KAY/O:1159x936', 'Killjoy:1257x941', 'Neon:649x1023', 'Skye:766x1006', 'Viper:840x1020', 'Yoru:920x1010', 'Lock:926x736']\nCustomCords=None\n#Note Use Custom Cords Generated with Cordsmaker.py")
        with open('theme/cords.txt','r') as file:
            cordsfile = file.read()
        with open('theme/cords.txt','w') as file:
            file.write(str(cordsfile.replace('None',str(cords))))  
            print(str(cordsfile.replace('None',str(cords))))
mouse.Listener(on_click=get_pos).start()


while True:
    time.sleep(50)
