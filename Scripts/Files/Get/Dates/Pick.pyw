with redirect_stdout(stdout):
	print(Break + Styles.Meta_Info_2 + "\n\nGetting file dates...", Styles.Reset)

#-=-=-=-#

Dates = Keep(Files)
Dates.pick()