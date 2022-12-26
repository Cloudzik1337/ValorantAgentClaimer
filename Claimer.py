import tkinter as tk
from tkinter import ttk 
import os, json, threading
from pynput import keyboard
from pynput.mouse import Button, Controller

import time, sys

root = tk.Tk()
root.iconbitmap('theme/purpeblue.ico')
root.resizable(False, False)
x_to_clikc = None
y_to_click = None
agent = None
kb = None
kb = None
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
    global toggle, x_to_clikc, y_to_click, delay
    while True:
        if toggle:
            mouse.position = (x_to_clikc, y_to_click)
            mouse.click(Button.left, 2)
            # time.sleep(0.01)
            time.sleep(float(delay))
            mouse.position = (974, 818)
            mouse.click(Button.left, 2)
            time.sleep(float(delay))


def on_press(key):
    global data, existsbef, agents, kb, delay, agent, toggle, x_to_clikc, y_to_click
    if str(key).strip("'") == kb:
        
        ags = ['Brimstone:589x934', 'Jett:669x928', 'Omen:746x924', 'Phoenix:838x932', 'Raze:912x931', 'Reyna:1016x931', 'Sage:1084x933', 'Sova:1180x925', 'Astra:1250x936', 'Breach:1330x931', 'Chamber:577x1011', 'Cypher:672x1014', 'Fade:744x1011', 'Harbor:838x1015', 'KAY/O:918x1014', 'Killjoy:999x1014', 'Neon:1087x1014', 'Skye:1178x1018', 'Viper:1259x1014', 'Yoru:1329x1019']

        for ag in ags:
            
            agentc, cords = ag.split(':')

            if agentc == agent:

                cordx, cordy = cords.split('x')

                x_to_clikc = cordx
                y_to_click = cordy
                toggle = not toggle
                break




data = ''

def apply():
    global data, existsbef, agents, kb, delay, agent


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


def showgui():
    global data, existsbef, agents, kb, delay, agent
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
