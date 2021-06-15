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
import time
from tkinter.filedialog import askopenfilename
import os.path, time
from winregistry import WinRegistry as Reg
reg = Reg()

# > Functions
def ActivityViewWindow():
  path = "HKEY_CURRENT_USER\\SOFTWARE\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Compatibility Assistant\\Store"
  readKey = reg.read_key(path) 
  ActivitySubWindow = Toplevel(windows)
  ActivitySubWindow.geometry("600x600")
  text = Text(ActivitySubWindow, wrap=tk.WORD, foreground="White")
  text.pack(expand=YES, fill=BOTH)
  text.insert(tk.END, f"{readKey}")
  scrollX = tk.Scrollbar(ActivitySubWindow, orient=tk.HORIZONTAL)
  scrollX.config(command=text.xview)
  text.configure(xscrollcommand=scrollX.set)
  scrollX.pack(side=tk.BOTTOM, fill=tk.X)

def LastModification():
  filename = askopenfilename()
  print("Last modified: %s" % time.ctime(os.path.getmtime(filename)))

def HelpWindow():
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
paperbinmBtn = TkinterCustomButton(text = "Paperbin LM", corner_radius = 10, command =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   LastModification)
paperbinmBtn.place(relx = 0.2, rely = 0.5, anchor = tk.CENTER)

# > Windows >  Definitions
windows.title('QuarentineDev - Main Window')
windows.geometry("800x600")
windows.resizable(False, False)
windows.tk.call('wm', 'iconphoto', windows._w, tk.PhotoImage(file='src/SSTOOLSlogo.png'))
windows.mainloop()
