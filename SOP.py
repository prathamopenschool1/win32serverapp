#!/usr/bin/env python3

from __future__ import print_function
from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter import ttk
import socket
import errno
import os
import subprocess
import time
import sys
import psutil
import requests

if sys.version_info[0] >= 3:
    import tkinter as tk
else:
    import Tkinter as tk

LARGE_FONT = ("Verdana", 12)


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def check_internet():
    url_check = 'http://www.hlearning.openiscool.org/api/crl/get/'
    timeout = 3
    try:
        _ = requests.get(url_check, timeout=timeout)
        return True
    except requests.ConnectionError:
        messagebox.showinfo("pratham", "please check your internet connection")
        sys.exit(0)


def check_port():
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 8080))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            messagebox.showinfo("SERVERAPP", "server is already running")
            if e.errno:
                sys.exit(0)
        else:
            messagebox.showinfo("SERVERAPP", e)

    s.close()


def stop_kolibri():
    try:
        os.system('kolibri stop')
        messagebox.showinfo("SERVERAPP", "kolibri server stopped")
    except Exception as stp:
        messagebox.showinfo("SERVERAPP", stp)


def start_kolibri():
    try:
        check_port()
        os.system('kolibri start')
        messagebox.showinfo("SERVERAPP", "kolibri server started")
    except Exception as str:
        messagebox.showinfo("SERVERAPP", str)


# def on_camera():
#     try:
#         os.system('sudo modprobe bcm2835-v4l2')
#         messagebox.showinfo("SERVERAPP", "camera is on")
#     except Exception as cam:
#         messagebox.showinfo("SERVERAPP", cam)


# def video_call():
#     try:
#         os.system('sudo service dnsmasq stop')
#         os.system('sudo modprobe bcm2835-v4l2')
#         check_internet()
#         try:
#             create_window()
#         except Exception as w:
#             messagebox.showinfo("SERVERAPP", w)
#     except Exception as vid:
#         messagebox.showinfo("SERVERAPP", vid)


# def create_window():
#     win = tk.Toplevel(window)
#     win.resizable(0, 0)
#     win.geometry("250x150")
#     # win.configure(bg='gray')
#     window_width = win.winfo_reqwidth()
#     window_height = win.winfo_reqheight()

#     position_right = int(win.winfo_screenwidth() / 2 - window_width / 2)
#     position_down = int(win.winfo_screenheight() / 2 - window_height / 2)

#     win.geometry("+{}+{}".format(position_right, position_down))

#     var = tk.IntVar()

#     choose = tk.Label(win, text="select a time for the call", padx=20, foreground='black')
#     choose.grid(row=0, column=0)

#     select1 = tk.Radiobutton(win, text="20 minutes", variable=var, value=1)
#     select1.grid(row=1, column=0)
#     select2 = tk.Radiobutton(win, text="30 minutes", variable=var, value=2)
#     select2.grid(row=2, column=0)
#     select3 = tk.Radiobutton(win, text="60 minutes", variable=var, value=3)
#     select3.grid(row=3, column=0)
#     select4 = tk.Radiobutton(win, text="90 minutes", variable=var, value=4)
#     select4.grid(row=4, column=0)

#     def select_value():
#         selection = var.get()
#         # print('Pushed the button!')
#         # print('var has value', selection)
#         text_dict = {
#             0: 0,
#             1: 20,
#             2: 30,
#             3: 60,
#             4: 90
#         }
#         global minute_to_get

#         if text_dict[selection] == 0:
#             messagebox.showinfo("SERVERAPP", "please select the time")
#             sys.exit(0)
#         else:
#             minute_to_get = text_dict[selection]
#         win.destroy()
#         site = "https://www.gmail.com/"
#         p = subprocess.Popen(['chromium-browser', site])
#         poll = p.poll()
#         time.sleep(120)

#         def countdown(n):
#             while n > 0:
#                 # print(n)
#                 n = n - 1
#                 if n == 300:
#                     window.call('wm', 'attributes', '.', '-topmost', '1')
#                     messagebox.showinfo("SERVERAPP", "browser will be closed in 5 minutes please logout or "
#                                                      "if you want to continue please setup another call")
#                 time.sleep(1)
#                 if checkIfProcessRunning('chromium-browser'):
#                     pass
#                 else:
#                     os.system('sudo service dnsmasq start')
#                     sys.exit(0)

#         countdown(60 * int(minute_to_get) + 300)
#         # countdown(int(minute_to_get))

#         p.kill()
#         # os.system('sudo service dnsmasq start')
#         if poll is None:
#             try:
#                 os.system('sudo service dnsmasq start')
#                 sys.exit(0)
#             except Exception as dn:
#                 messagebox.showinfo("SERVERAPP", dn)

#     ok_btn = tk.Button(win, text='OK', width=10, command=select_value)
#     ok_btn.grid(row=7, column=0)


window = Tk()

window.wm_title("SERVERAPP")

window.resizable(0, 0)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

window.configure(bg="black")

start = Button(window, text="Start Kolibri", width=15, foreground='green', background='black', command=start_kolibri)
start.grid(row=1, column=0)

stop = Button(window, text="Stop Kolibri", width=15, foreground='green', background='black', command=stop_kolibri)
stop.grid(row=1, column=1)

# camera = Button(window, text="Turn on camera", width=15, foreground='green', background='black', command=on_camera)
# camera.grid(row=2, column=0)

# video = Button(window, text="Video Call", width=15, foreground='green', background='black', command=video_call)
# video.grid(row=2, column=1)

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

window.geometry("+{}+{}".format(positionRight, positionDown))
# window.geometry("350x100")

window.mainloop()
