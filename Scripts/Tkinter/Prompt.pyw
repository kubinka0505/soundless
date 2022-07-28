Selection = msgbox.askyesnocancel(
	"Warning",
	"""
	Operations made on the WAV files are irreversible and made in place.

	Selection action:
	    Proceed - files
	    Decline - directory
	"""[1:-1].replace("\t", ""),
	icon = "warning",
	default = "no"
)

if Selection == None:
	raise Error("\nProgram usage aborted")
elif Selection == False:
	Selection = "Directory"
else:
	Selection = "File"

print("{1}Dialog will ask for:\t{2}{0}{3}".format(
	Selection,
	Styles.Info, Styles.Warning, Styles.Reset,
	)
)

if Selection == "Directory":
	Ask_Recursive = msgbox.askyesno(
		"Confirm",
		"Optimize files in subdirectories?",
		icon = "question",
		default = "no"
	)

	Type_Processing = Styles.Warning + "Iterative"
	if Ask_Recursive:
		args.recursive = 1
		Type_Processing = Styles.Error + "Recursive"
	print("{1}Selected processing:\t{0}{2}".format(
		Type_Processing,
		Styles.Info, Styles.Reset
		)
	)

	args.input = fd.askdirectory(
		title = "Select directory with WAV files{0}".format(
			"[Recursive]" if Type_Processing == "Recursive" else ""
		),
		initialdir = GUI_Initial_Directory
	)
if Selection == "File":
	args.input = fd.askopenfilenames(
		title = "Select WAV files",
		initialdir = GUI_Initial_Directory,
		filetypes = (
			("Microsoft Wave files", "*.wav"),
			("All files", "*.*")
		)
	)

if not args.input:
	raise Error(f"\n{Selection} selection aborted")