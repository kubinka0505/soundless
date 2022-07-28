with redirect_stdout(stdout):
	print()
	for Package in ["FFmpeg", "SoX"]:
		Package_Name = Package
		Package = Get_Package(Package_Name)
		#-=-=-=-#
		if Package:
			print("{2}{0} path:\t\t{3}{1}{4}".format(
				Package_Name,
				FilePath(Package).censor(),
				Styles.Info, Styles.OK, Styles.Reset
				)
			)
			exec(f'{Package_Name} = r"{Package}"')
		else:
			Missing_Package_Message = f'Install it. ("{Package_Name.lower()}").'
			if OS.startswith("win"):
				Missing_Package_Message = 'Add it to "PATH" environment variable'
			#-=-=-=-#
			raise Error(
				Package_Name + f" not found!\n{Missing_Package_Message}")

#-=-=-=-#

FFmpeg += " -hide_banner -loglevel "
if args.quiet:
	FFmpeg += "-8"
	SoX += " -V0"
else:
	FFmpeg += "0"