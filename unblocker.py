import time
import os
from tkinter import *
import webbrowser
import ctypes
webbrowser.open('https://blackscreen.app/')
time.sleep(2)
ctypes.windll.user32.MessageBoxW(None, u"this is a unblocker", u"unblocker", 0)
ctypes.windll.user32.MessageBoxW(None, u"do u want to continue", u"unblocker", 1)
ctypes.windll.user32.MessageBoxW(None, u"unblocker is activated", u"unblocker", 0)
ctypes.windll.user32.MessageBoxW(None, u"ublocking everything...", u"unblocker", 0)
ctypes.windll.user32.MessageBoxW(None, u"      almost done       ", u"unblocker", 0)
ctypes.windll.user32.MessageBoxW(None, u"    loading...   ", u"unblocker", 0)
ctypes.windll.user32.MessageBoxW(None, u"    done👍  ", u"unblocker", 0)
time.sleep(2)
ctypes.windll.user32.MessageBoxW(None, u"    this is a prank🤪    ", u"unblocker", 0)
ctypes.windll.user32.MessageBoxW(None, u"  have fun   ", u"unblocker", 0)
webbrowser.open('https://i.pinimg.com/236x/56/21/7b/56217b1ef6a69a2583ff13655d48bc53.jpg')
import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

for i in range(1, 2):
    pos = abs((start_pos - i*90) % 360)
    screen.rotate_to(pos)
    time.sleep(1.5)
   

