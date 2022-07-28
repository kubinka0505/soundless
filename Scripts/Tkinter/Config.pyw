tk = Tk()
tk.withdraw()
tk.call("wm", "iconphoto", tk._w, PhotoImage(
	file = os.path.join(
			__BaseDir,
			"Documents/Pictures/Main/Icon.png"
		)
	)
)