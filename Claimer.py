import tkinter as tk
from tkinter import ttk 
import os, json, threading
from pynput import keyboard
from pynput.mouse import Button, Controller
from playsound import playsound
import time, sys
ags = []
CustomCords = None
if not os.path.exists('theme/cords.txt'):
    
    with open('theme/cords.txt','a+')as cords:
        cords.write("ags = ['Brimstone:653x838', 'Jett:748x845', 'Omen:827x844', 'Phoenix:912x845', 'Raze:1003x843', 'Reyna:1081x847', 'Sage:1178x838', 'Sova:1248x845', 'Astra:643x925', 'Breach:760x924', 'Chamber:826x922', 'Cypher:917x924', 'Fade:998x926', 'Harbor:1086x937', 'KAY/O:1159x936', 'Killjoy:1257x941', 'Neon:649x1023', 'Skye:766x1006', 'Viper:840x1020', 'Yoru:920x1010', 'Lock:926x736']\nCustomCords=None\n#Note Use Custom Cords Generated with Cordsmaker.py")
with open('theme/cords.txt','r')as cords:
    cordsr = cords.read()
    exec(cordsr)
    if cordsr != '':
        if CustomCords != None:
            ags = CustomCords

        Lockx, Locky = str(ags[-1]).split(':')[1].split('x') 
        ags.remove(ags[-1])
        


root = tk.Tk()
root.iconbitmap('theme/purpeblue.ico')
root.resizable(False, False)
x_to_clikc = None
y_to_click = None
agent = None
kb = None
kb = None
curr_path = 'theme/agents/Brimstone.png'
delay = None
root.attributes("-alpha",0.95)
root.title('Cloud Valorant Agent Picker ')

def_button = 'x'
toggle = False

def t1():
    mouse = Controller()
    t = keyboard.Listener(on_press=on_press)
    t.daemon =True
    t.start()
    global toggle, x_to_clikc, y_to_click, delay, Lockx, Locky
    while True:
        if toggle:
            mouse.position = (x_to_clikc, y_to_click)
            mouse.click(Button.left, 2)
            time.sleep(float(delay))  
            mouse.position = (Lockx, Locky)
            mouse.click(Button.left, 2)
            time.sleep(float(delay))


def on_press(key):
    global data, existsbef, agents, kb, delay, agent, toggle, x_to_clikc, y_to_click, l
    if str(key).strip("'") == kb:
        
        

        for ag in ags:
            
            agentc, cords = ag.split(':')

            if agentc == agent:

                cordx, cordy = cords.split('x')

                x_to_clikc = cordx
                y_to_click = cordy
                toggle = not toggle
                break
              
        if toggle:
            toggleon = 'ON'
            l.configure(text=f"\n\nStatus:\n{toggleon}", fg='Green')
            playsound('theme/enable.wav')
            
        else:
            toggleon = 'OFF'
            l.configure(text=f"\n\nStatus:\n{toggleon}", fg='White')
            playsound('theme/disable.wav')
            

    
        #l = tk.Label(keybind_frame, text = f"\n\nStatus:\n{toggleon}")
        
def updateimg(curr_path):
    global canvas, image, agent
    if agent == 'KAY/O':
        curr_path = 'theme/agents/KAYO.png'
    image = tk.PhotoImage(file=curr_path)
    canvas.create_image(64,64,image=image)
    canvas.update()

data = ''

def apply():
    global data, existsbef, agents, kb, delay, agent, canvas, curr_path, image


    agent = combo_box.get()
    delay = spinbox.get()
    kb = entrykb.get()

    
    with open('config.txt', 'a+') as file:
        pass

    with open('config.txt', 'w')as file:
        jsonbuild = {
            'agent': agent,
            'delay': delay,
            'keybind': kb
        }
        file.write(json.dumps(jsonbuild))
        curr_path = f'theme/agents/{agent}.png'
        updateimg(curr_path=curr_path)







apply_frame = tk.LabelFrame(root, text="Apply Changes",padx=20, pady=20)
apply_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")

apply_button = ttk.Button(apply_frame, text='Save Changes ', command=apply)
apply_button.pack()

agents_frame = tk.LabelFrame(root, text="Choose Agent",padx=20, pady=20)
agents_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
agents = ['Brimstone', 'Jett', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Sova', 'Astra', 'Breach', 'Chamber', 'Cypher', 'Fade', 'Harbor', 'KAY/O', 'Killjoy', 'Neon', 'Skye', 'Viper', 'Yoru']
combo_box = ttk.Combobox(agents_frame, state='readonly', values=agents)
combo_box.current(0)
combo_box.pack()

canvas = tk.Canvas(agents_frame, width = 128, height = 128)
canvas.pack()
image = tk.PhotoImage(file=curr_path)
canvas.create_image(64,64,image=image)


spinbox_frame = tk.LabelFrame(root, text="Delay",padx=20, pady=20)
spinbox_frame.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
spinbox = ttk.Spinbox(spinbox_frame, from_=0.009, to=10, increment=0.1)
spinbox.insert(0,0.1)
spinbox.pack()


keybind_frame = tk.LabelFrame(root, text="Keybind",padx=20, pady=20)
keybind_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
entrykb = ttk.Entry(keybind_frame)
entrykb.insert(0, def_button)
entrykb.pack()
if toggle:
    toggleon = 'ON'
    fg = 'Green'
else:
    toggleon = 'OFF'
    fg = 'White'
l = tk.Label(keybind_frame, text = f"\n\nStatus:\n{toggleon}", fg=fg)
l.config(font =("Impact", 14, ))
l.pack()


def showgui():
    global data, existsbef, agents, kb, delay, agent, curr_path
    with open('config.txt', 'a') as file:
        pass
    if os.path.exists('config.txt') and os.path.getsize('config.txt') != 0:
        with open('config.txt', 'r') as file:
            
                datafile = file.read()
                
                data = json.loads(datafile)


                entrykb.delete(0, 'end')
                spinbox.delete(0, 'end')
                
                def change_to_agent(agent: str):    
                    agents = ['Brimstone', 'Jett', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Sova', 'Astra', 'Breach', 'Chamber', 'Cypher', 'Fade', 'Harbor', 'KAY/O', 'Killjoy', 'Neon', 'Skye', 'Viper', 'Yoru']
                    for i in range(len(agents)):
                        if agent == agents[i]:
                            return i
                agent_to_put = change_to_agent(data['agent'])
                combo_box.current(agent_to_put)
                entrykb.insert(0, data['keybind'])
                spinbox.insert(0, data['delay'])
                agent = data['agent']
                curr_path = f'theme/agents/{agent}.png'
                updateimg(curr_path)
                kb = data['keybind']
                delay = data['delay']
    else:
        pass

showgui()

root.tk.call("source", "azure.tcl")

root.tk.call("set_theme", "dark")

threading.Thread(target=t1, daemon=True).start()

root.mainloop()


sys.exit()
