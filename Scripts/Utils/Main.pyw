session = Session()
session.headers.update(
	{
		"User-Agent":
		"Mozilla/5.0 (Windows NT 10.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
	}
)
get = session.get

OS = os.sys.platform.lower()
os.system("")

#-=-=-=-#

class Styles:
	"""Colored Prints"""
	Error = "#C10"
	OK = "#0C0"
	Flaw = "#F36"
	Info = "#4AF"
	Meta_Info = "#999"
	Meta_Info_2 = "#B5F"

_CLS = Styles
for Variable in list(vars(_CLS))[2:-2]:
	exec('{0}.{1} = "{2}"'.format(
		_CLS.__name__, Variable,
		fg(*IC.getrgb(Color(getattr(_CLS, Variable)).hex_l))
		)
	)

_CLS.Warning = fg(*IC.getrgb("#FC0"))
_CLS.Reset = fg.rs

#-=-=-=-#

def Get_Console_Output(Command: str) -> list:
	"""Returns console output from Popen"""
	Process = Popen(Command, stdout = PIPE, stderr = PIPE, shell = 1)
	Output, Error = Process.communicate()
	#-=-=-=-#
	return sorted(list(set([Element.decode("U8") for Element in [Output, Error] if Element])))

def Get_Channels(Input: str) -> int:
	"""Get audio channels from audio file."""
	Mono_Output = Get_Console_Output(f'"{FFmpeg}" -i "{Input}" -filter_complex "[0:a]channelsplit=channel_layout=stereo[left][right]" -map "[left]" -f md5 - -map "[right]" -f md5 -')
	#-=-=-=-#
	Channels = 2
	if len(list(set(Mono_Output[0].replace("MD5=", "\n").split("\n")[1::2]))) < 2:
		Channels = 1
	return Channels

def Get_Package(Name: str) -> str:
	"""Locate package in "PATH" environment variable or check if it is installed."""
	Name = Name.lower()
	Package = None
	#-=-=-=-#
	if OS.startswith("win"):
		Variables = os.environ["PATH"].split(os.pathsep)
		for Variable in Variables:
			if Name + ".exe" in Variable.lower():
				Name = Variable
				break
		if os.path.exists(Name):
			Package = FilePath(Name).get()
	else:
		import apt
		cache = apt.Cache() 
		if cache[Name].is_installed:
			Package = Name
	#-=-=-=-#
	return Package

def File_Size(Bytes: float) -> str:
	"""Returns human-readable file size"""
	for Unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
		if Bytes < 1024: break
		Bytes /= 1024
	#-=-=-=-#
	return str(round(Bytes, 2)) + " " + Unit

class FilePath:
	def __init__(self, Path_):
		self.Path = os.path.normpath(Path_)

	def get(self) -> str:
		"""Path fetching with additional support of variables and user expansion"""
		return str(Path(os.path.abspath(os.path.expanduser(os.path.expandvars(self.Path)))).resolve())

	def censor(self) -> str:
		"""Censors path from user name."""
		if OS.startswith("win"):
			String = "%UserProfile%"
		else:
			String = "~"
		#-=-=-=-#
		Path = self.Path.replace(
			FilePath("~").get(), String
		)
		return Path

def Number_Suffix(Number: float) -> float:
	"""Converts number with suffixes to float."""
	Number = str(Number).lower()

	Units = {"k" : 1E3, "m": 1E6}
	Multiplicator = 1

	while Number[-1] in Units:
		Multiplicator *= Units[Number[-1]]
		Number = Number[:-1]
	return float(Number) * Multiplicator

def Clamp(Number: float, Minimum: float, Maximum: float) -> float:
	"""Limits `Number` in range (`Minimum`, `Maximum`)."""
	return max(min(Maximum, Number), Minimum)

#-=-=-=-#

exit_ = SystemExit
Error = lambda exc: exit_(Styles.Error + str(exc) + "." + Styles.Reset)

GUI_Initial_Directory = []
for Directory in ["Documents", "Downloads", "Desktop"]:
	Directory = "~/" + Directory
	Directory = FilePath(Directory).get()
	#-=-=-=-#
	GUI_Initial_Directory += [Directory]

GUI_Initial_Directory = sorted(GUI_Initial_Directory, key = os.path.getmtime)[-1]

#-=-=-=-#

if OS.startswith("win32"):
	os.system(f"title {__name__} v{__version__}")
	
Random_String = "".join(choice(ascii_letters + digits) for x in range(5))
Break = Styles.Reset + "-=" * 16 + "-"