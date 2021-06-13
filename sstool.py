"""
__________________________
|                        |
|    By: QuarentineDev   |
|                        |
--------------------------

   SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS
 SS:::::::::::::::S SS:::::::::::::::S
S:::::SSSSSS::::::SS:::::SSSSSS::::::S
S:::::S     SSSSSSSS:::::S     SSSSSSS
S:::::S            S:::::S
S:::::S            S:::::S
 S::::SSSS          S::::SSSS                      eeeee eeeee eeeee e     eeeee 
  SS::::::SSSSS      SS::::::SSSSS                   8   8  88 8  88 8     8   "
    SSS::::::::SS      SSS::::::::SS                 8e  8   8 8   8 8e    8eeee
       SSSSSS::::S        SSSSSS::::S                88  8   8 8   8 88       88
            S:::::S            S:::::S               88  8eee8 8eee8 88eee 8ee88
            S:::::S            S:::::S
SSSSSSS     S:::::SSSSSSSS     S:::::S
S::::::SSSSSS:::::SS::::::SSSSSS:::::S
S:::::::::::::::SS S:::::::::::::::SS
 SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS

"""


# > Imports
import tkinter as tk
from tkinter_custom_button import TkinterCustomButton
from tkinter import *
from PIL import ImageTk, Image
import os

# > Functions
def ActivityViewWindow():
  activityWindow = Toplevel(windows)
  activityWindow.title('QuarentineDev SS TOOLS - Activity View')

def paperbin_last_modification():
  pass

# > Variables
windows = tk.Tk()
logobg = ImageTk.PhotoImage(Image.open('src/SSTOOLSlogo.png'))
logoLABELbg = Label(windows, image = logobg, anchor = tk.CENTER)
logoLABELbg.pack()
logoLABELbg.place(relx = 0.5, rely = 0.150, anchor = tk.CENTER)

# > Other Windows Properties
ActivityWindow = Label(windows)
ActivityWindow.pack(pady = 10)
ActivityWindowBtn = TkinterCustomButton(text = "Activity View", corner_radius = 10, command = ActivityViewWindow)
ActivityWindowBtn.place(relx = 0.2, rely = 0.4, anchor = tk.CENTER)
#ActivityWindowBtn = Button(windows, text = 'Activity View', command = ActivityViewWindow)
#ActivityWindowBtn.pack(pady = 10)

paperbinmwindow = Label(windows)
paperbinmwindow.pack(pady = 10)
paperbinmBtn = TkinterCustomButton(text = "Paperbin LM", corner_radius = 10, command = paperbin_last_modification) #Paperbin LM = paperbin last modification
paperbinmBtn.place(relx = 0.2, rely = 0.5, anchor = tk.CENTER)

# > Windows >  Definitions
windows.title('QuarentineDev - Main Window')
windows.geometry("800x600")
windows.resizable(False, False)
windows.tk.call('wm', 'iconphoto', windows._w, tk.PhotoImage(file='src/SSTOOLSlogo.png'))
windows.mainloop()
