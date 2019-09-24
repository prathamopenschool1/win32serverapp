#!/usr/bin/env python3

from __future__ import print_function
from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter import ttk
import socket
import errno
import os
import csv
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


def superuser():

    file = "C:\prathamdata\Csvfiles\output.csv"

    i=0
    csvfile = open(file, 'r+')

    data = csv.reader(csvfile, delimiter=',')

    messagebox.showinfo("SERVERAPP", "wait while user is being created")

    for line in data:
        user_creation='kolibri manage shell -c "from kolibri.auth.models import FacilityUser; FacilityUser.objects.create_superuser(\'' + line[0] + '\',\'' + line[1] + '\')"'
        os.system(user_creation)
        print(i)
        i = i+1

    csvfile.close()

    messagebox.showinfo("SERVERAPP", "user creation completed!")


def coach():

    messagebox.showinfo("SERVERAPP","wait while youth is being created")

    file = 'kolibri manage importusers C:\prathamdata\Csvfiles\learners.csv'
    os.system(file)

    messagebox.showinfo("SERVERAPP", "youth creation completed!")


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

superusers = Button(window, text="Create Users", width=15, foreground='green', background='black', command=superuser)
superusers.grid(row=2, column=0)

youth = Button(window, text="Create Youth", width=15, foreground='green', background='black', command=coach)
youth.grid(row=2, column=1)

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

window.geometry("+{}+{}".format(positionRight, positionDown))
# window.geometry("350x100")

window.mainloop()
