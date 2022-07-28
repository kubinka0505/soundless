Title = "Success"
Messages = ["de", ""]

if Size_In <= Size_Out:
	Title = "Failure"

#-=-#

if Size_In < Size_Out:
	Messages = ["in", "+"]
	msgbox.showinfo = msgbox.showwarning

Messages += [Styles.Error + "Files were not optimized despite performed operations."]

if Size_In != Size_Out:
	Messages[-1] = \
		(Styles.OK if Messages[0] == "de" else Styles.Error) \
		+ "Size of {0} files {1}creased from {2} to {3} ({4}{5}%)".format(
			len(Files), Messages[0], File_Size(Size_In), File_Size(Size_Out), Messages[1], Percentage
		)

Messages += ["Runtime: " + Run_Time + "ms"]

print(
	"\nMessage\n\t"
	+ Messages[-2]
	+ "\n\t"
	+ Messages[-1]
	+ Styles.Reset
)

#-=-#

Open_Target_Directory = msgbox.askyesno(
	Title,
	Messages[-2].split("0m")[-1]
	+ "\n"
	+ Messages[-1]
	+ "\n\nOpen containing directory?",
	icon = "info"
)

if Open_Target_Directory:
	if Selection == "file":
		Latest_Directory = os.path.dirname(sorted(Files, key = len)[0])
	#-=-=-=-#
	Command = "nautilus"
	if OS.startswith("win32"):
		Command = r"start /max C:\Windows\explorer.exe"
	#-=-=-=-#
	os.system(f'{Command} "{Latest_Directory}"')