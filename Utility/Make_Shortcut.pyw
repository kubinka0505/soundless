exec(open("__init__.pyw", encoding = "U8").read())
with redirect_stdout(None):
	from pyshortcuts import make_shortcut

Initial_Directory = os.path.abspath(os.path.expanduser("~/Desktop"))

#-=-=-=-#

Icon_HQ = os.path.abspath(Icon.replace("Icon", "Icon_HQ"))
if OS.startswith("win"):
	Icon_HQ += ".ico"
else:
	Icon_HQ += ".png"

Script = [os.path.abspath("../" + File)
	for File in next(os.walk(".."))[2]
		if "py" in File.lower().split(".")[-1]
][-1]

#-=-=-=-#

Directory = fd.askdirectory(
	title = "Select directory to create shortcut in",
	initialdir = Initial_Directory
)
Directory = os.path.abspath(Directory)

if Directory == os.getcwd():
	Directory = Initial_Directory
	raise SystemExit("\nDirectory selection aborted.")

os.chdir(Directory)

#-=-=-=-#

Name = "soundless"
try:
	for Shortcut in next(os.walk("."))[2]:
		if Shortcut.startswith(Name):
			print("Removing previous shortcut...")
			os.remove(os.path.abspath(Shortcut))
			break
except IndexError:
	pass

#-=-=-=-#

print("Making shortcut...")
make_shortcut(
	Script, Name,
	"Optimize WAV files",
	Icon_HQ, Directory,
	terminal = 1 if Script.endswith("py") else 0,
	startmenu = 0
)

#-=-=-=-#

Message = 'Shortcut successfully created in the "' + Directory.split(os.sep)[-1] + '" directory.'

print(Message)
msgbox.showinfo("Success", Message)