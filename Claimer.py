import tkinter as tk
from tkinter import ttk
import os
import json
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller
from playsound import playsound
import time
import sys
import logging

log_level = logging.CRITICAL #DO NOT TOUCH IF YOU DONT KNOW WHAT YOU ARE DOING


logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
try:

    root = tk.Tk()
    root.iconbitmap('theme/purpeblue.ico')
    root.resizable(False, False)
    x_to_click = None
    y_to_click = None
    agent = None
    kb = None
    toggle = False
    current_path = 'theme/agents/Brimstone.png'
    delay = 0
    root.attributes("-alpha", 0.95)
    root.title('Cloud Valorant Agent Picker ')
    logging.debug('title set to Cloud Valorant Agent Picker')
    def_button = 'x'
    ags = []
    CustomCords = None

    if not os.path.exists('theme/cords.txt'):
        with open('theme/cords.txt', 'a+') as cords:
            cords.write(
                "ags = ['Brimstone:584x928', 'Jett:670x925', 'Omen:750x924', 'Phoenix:827x926', 'Raze:915x936', 'Reyna:1010x935', 'Sage:1100x929', 'Sova:1172x935', 'Astra:1256x924', 'Breach:1332x924', 'Chamber:580x1012', 'Cypher:662x1008', 'Fade:739x1020', 'Harbor:837x1006', 'KAY/O:912x1013', 'Killjoy:1004x1008', 'Neon:1070x1014', 'Skye:1172x1014', 'Viper:1241x1008', 'Yoru:1349x1023', 'Lock:929x813']\nCustomCords=None\n#Note Use Custom Cords Generated with Cordsmaker.py")
            logging.debug('loaded 1920x1080 cords to cords.txt')
    with open('theme/cords.txt', 'r') as cords:
        cords_read = cords.read()
        exec(cords_read)
        if cords_read != '':
            if CustomCords is not None:
                ags = CustomCords
                logging.debug('Custom Cords Loaded')
            else:
                logging.debug('Default Cords Loaded')
            Lockx, Locky = str(ags[-1]).split(':')[1].split('x')
            logging.debug(f'Lock Cords Loaded {Lockx} {Locky}')
            ags.remove(ags[-1])


    def t1():

        mouse = Controller()
        t = keyboard.Listener(on_press=on_press)
        logging.debug('Started Keyboard Listener')
        t.daemon = True
        t.start()
        global toggle, x_to_click, y_to_click, delay, Lockx, Locky
        while True:
            if toggle:
                mouse.position = (x_to_click, y_to_click)
                mouse.click(Button.left, 2)
                time.sleep(float(delay))
                mouse.position = (Lockx, Locky)
                mouse.click(Button.left, 2)
                time.sleep(float(delay))
                logging.debug(f'Clicked {x_to_click} {y_to_click}')


    def on_press(key):
        global data, agents, kb, delay, agent, toggle, x_to_click, y_to_click, toggle_state
        if str(key).strip("'") == kb:

            for ag in ags:

                agentc, cordsagent = ag.split(':')

                if agentc == agent:
                    cordx, cordy = cordsagent.split('x')

                    x_to_click = cordx
                    y_to_click = cordy
                    logging.debug(f'Agent {agent} was found in cords.txt')
                    toggle = not toggle
                    break

            if toggle:
                istoggled = 'ON'
                toggle_state.configure(text=f"Status:\n{istoggled}", fg='Green')
                playsound('theme/enable.wav')
                logging.debug(f'Agent {agent} was toggled ON')

            else:
                istoggled = 'OFF'
                toggle_state.configure(text=f"Status:\n{istoggled}", fg='Red')
                playsound('theme/disable.wav')
                logging.debug(f'Agent {agent} was toggled OFF')

            # toggle_state = tk.Label(keybind_frame, text = f"\n\nStatus:\n{istoggled}")


    def updateimg(current_path):
        global canvas, image, agent
        if agent == 'KAY/O':
            current_path = 'theme/agents/KAYO.png'
        image = tk.PhotoImage(file=current_path)
        canvas.create_image(64, 64, image=image)
        logging.debug(f'Agent {agent}.png was loaded')
        canvas.update()


    def refresh_text(agent, kb, delay):
        global text
        text.configure(text=f'Current Agent - {agent}\nKeybind - {kb}\nDelay - {delay}')
        logging.debug('Text was refreshed')

    data = ''


    def apply():
        global data, agents, kb, delay, agent, canvas, current_path, image, text

        agent = combo_box.get()
        logging.debug(f'Agent {agent} was selected')
        delay = spinbox.get()
        logging.debug(f'Delay {delay} was selected')
        kb = entrykb.get()
        logging.debug(f'Keybind {kb} was selected')
        refresh_text(agent, kb, delay)

        logging.debug('Obtain data from widgets')
        with open('theme/config.txt', 'a+') as file:
            logging.debug('Config.txt was touched')
            pass

        with open('theme/config.txt', 'w') as file:
            jsonbuild = {
                'agent': agent,
                'delay': delay,
                'keybind': kb
            }
            file.write(json.dumps(jsonbuild))
            current_path = f'theme/agents/{agent}.png'
            updateimg(current_path=current_path)
            logging.debug(f'config.txt was updated with {jsonbuild}')


    apply_frame = tk.LabelFrame(root, text="Apply Changes", padx=20, pady=20)
    apply_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
    logging.debug('Apply Frame was created')
    apply_button = ttk.Button(apply_frame, text='Save Changes ', command=apply)
    apply_button.pack()
    logging.debug('Apply Button was created')
    agents_frame = tk.LabelFrame(root, text="Choose Agent", padx=20, pady=20)
    agents_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
    agents = ['Brimstone', 'Jett', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Sova', 'Astra', 'Breach', 'Chamber',
              'Cypher', 'Fade', 'Harbor', 'KAY/O', 'Killjoy', 'Neon', 'Skye', 'Viper', 'Yoru']
    combo_box = ttk.Combobox(agents_frame, state='readonly', values=agents)
    combo_box.current(0)
    combo_box.pack()
    logging.debug('Agent Combobox was created')
    canvas = tk.Canvas(agents_frame, width=128, height=128)
    canvas.pack()
    image = tk.PhotoImage(file=current_path)
    canvas.create_image(64, 64, image=image)
    logging.debug('Agent Image was created')
    spinbox_frame = tk.LabelFrame(root, text="Delay", padx=20, pady=20)
    spinbox_frame.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
    spinbox = ttk.Spinbox(spinbox_frame, from_=0.009, to=10, increment=0.1)
    spinbox.insert(0, '0.1')
    spinbox.pack()
    logging.debug('Delay Spinbox was created')
    keybind_frame = tk.LabelFrame(root, text="Keybind", padx=20, pady=20)
    keybind_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
    entrykb = ttk.Entry(keybind_frame)
    entrykb.insert(0, def_button)
    entrykb.pack()
    logging.debug('Keybind Entry was created')
    if toggle:
        istoggled = 'ON'
        fg = 'Green'
    else:
        istoggled = 'OFF'
        fg = 'Red'

    text = tk.Label(keybind_frame, text=f'Current Agent - {agent}\nKeybind - {kb}\nDelay - {delay}', fg='white')
    text.config(font=('Tahoma', 10, 'bold'))
    text.pack()
    toggle_state = tk.Label(keybind_frame, text=f"Status:\n{istoggled}", fg=fg)

    toggle_state.config(font=("Impact", 14,))
    toggle_state.pack()


    def showgui():
        global data, agents, kb, delay, agent, current_path
        with open('theme/config.txt', 'a') as file:
            pass
        if os.path.exists('theme/config.txt') and os.path.getsize('theme/config.txt') != 0:
            with open('theme/config.txt', 'r') as file:

                datafile = file.read()
                data = json.loads(datafile)
                entrykb.delete(0, 'end')
                spinbox.delete(0, 'end')

                def change_to_agent(agent: str):
                    agents = ['Brimstone', 'Jett', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Sova', 'Astra', 'Breach',
                              'Chamber', 'Cypher', 'Fade', 'Harbor', 'KAY/O', 'Killjoy', 'Neon', 'Skye', 'Viper', 'Yoru']
                    for i in range(len(agents)):
                        if agent == agents[i]:
                            return i

                agent_to_put = change_to_agent(data['agent'])
                combo_box.current(agent_to_put)
                entrykb.insert(0, data['keybind'])
                spinbox.insert(0, data['delay'])
                agent = data['agent']
                current_path = f'theme/agents/{agent}.png'
                updateimg(current_path)
                kb = data['keybind']
                delay = data['delay']
                refresh_text(agent, kb, delay)
                logging.debug('Data was loaded from config.txt')
        else:
            pass


    showgui()
    root.tk.call("source", "azure.tcl")
    logging.debug('Azure theme was loaded')
    root.tk.call("set_theme", "dark")
    logging.debug('Azure theme was set to dark')
    threading.Thread(target=t1, daemon=True).start()
    logging.debug('Helper Thread was started')
    root.mainloop()
    logging.debug('Quiting properly all threads and processes were terminated')
    sys.exit()
except Exception as e:

    logging.critical(f'Error: {e}')
    time.sleep(0.5)

    print(f'Please Create a issue on github with the following error: {e}')
    input('Press Enter to exit')
