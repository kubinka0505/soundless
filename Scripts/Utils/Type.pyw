if len(os.sys.argv) == 1:
	Type_Interface = "GUI"
else:
	Type_Interface = "CLI"

Interface = "{1}Inteface type:\t\t{2}{0}{3}".format(
	Type_Interface,
	Styles.Info, Styles.OK, Styles.Reset
)