try:
	Counter = 0
	for Input in Files:
		exec(open_("Files/Process/Initialize"))
		#-=-=-=-#
		with redirect_stdout(stdout):
			exec(open_("Files/Process/Main"))
			Counter += 1
except KeyboardInterrupt:
	print("\a{2}Interrupted by user, {3}[{0}/{1}]{2} files optimized{4}".format(
		Counter, len(Files),
		Styles.Flaw, Styles.Warning, Styles.Reset
		)
	)