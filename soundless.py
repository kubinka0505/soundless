"""soundless

WAV files optimizer"""
import os
from sty import fg
from colour import Color
from pathlib import Path
from random import choice
from time import sleep, time
from requests import Session
from datetime import timedelta
from filedate.Utils import Keep
from PIL import ImageColor as IC
from mutagen import File as mFile
from subprocess import Popen, PIPE
from contextlib import redirect_stdout
from string import ascii_letters, digits
from argparse import ArgumentParser, HelpFormatter, SUPPRESS
from tkinter import Tk, PhotoImage, messagebox as msgbox, filedialog as fd
__BaseDir = os.path.abspath(os.path.dirname(__file__))

#-=-=-=-#

__name__		= open(__file__).readlines()[0].lstrip('"').rstrip("\n")
__author__		= "kubinka0505"
__version__		= "1.1"
__date__		= "20.07.2022"
__license__		= "GPL v3"
__status__		= "Mature"

#-=-=-=-#

open_ = lambda File: open(os.path.join(__BaseDir, "Scripts", File + ".pyw"), encoding = "U8").read()

exec(open_("Utils/Main"))
exec(open_("Utils/Type"))

if Type_Interface == "CLI":
	exec(open_("ArgParse"))
else:
	URL = 0
	class args:
		channels = c = 0
		bit_depth = 0
		samplerate = 0
		normalize = -1
		recursive = 0
		quiet = 0
	stdout = os.sys.stdout

with redirect_stdout(stdout):
	print(Interface)
	if Type_Interface == "CLI":
		exec(open_("ArgParse"))
	else:
		exec(open_("Tkinter/Config"))
		exec(open_("Tkinter/Prompt"))

#-=-=-=-#

Run_Time = time()

exec(open_("Files/Get/Packages"))
exec(open_("Files/Get/Main"))
exec(open_("Files/Get/Dates/Pick"))
exec(open_("Files/Process/Setup"))
exec(open_("Files/Get/Dates/Drop"))

Run_Time = timedelta(seconds = time() - Run_Time)
Run_Time = str(Run_Time)[2:-3]

print("\n" + Break)

if Type_Interface == "GUI":
	exec(open_("Tkinter/Messages"))
else:
	with redirect_stdout(stdout):
		print("\nRuntime\n\t{1}{0}{2}".format(
			Run_Time,
			Styles.Info, Styles.Reset
			)
		)