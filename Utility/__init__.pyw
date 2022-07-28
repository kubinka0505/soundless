import os
from contextlib import redirect_stdout
from tkinter import Tk, PhotoImage, filedialog as fd, messagebox as msgbox
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#-=-=-=-#

Icon = "../Documents/Pictures/Main/Icon"

#-=-=-=-#

OS = os.sys.platform.lower()

tk = Tk()
tk.withdraw()
try:
	tk.call("wm", "iconphoto", tk._w, PhotoImage(file = Icon + ".png"))
except:
	pass